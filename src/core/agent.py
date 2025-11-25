"""Gemini API communication layer"""

import asyncio
import json
import re
from typing import Any, Dict, Optional, List

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from src.config.settings import settings
from src.utils.exceptions import GeminiAPIError
from src.utils.logger import setup_logger

logger = setup_logger()

# ============================================================
# RATE LIMITER (Güncellendi)
# ============================================================
class RateLimiter:
    """Simple async rate limiter"""

    def __init__(self, calls_per_minute: int):
        self.min_interval = 60.0 / calls_per_minute
        self.last_call_time = 0.0
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            # Python 3.10+ uyumlu loop alma yöntemi
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.get_event_loop()
            
            now = loop.time()
            elapsed = now - self.last_call_time
            
            if elapsed < self.min_interval:
                await asyncio.sleep(self.min_interval - elapsed)

            self.last_call_time = loop.time()


# ============================================================
# GEMINI AGENT (ASENKRON & JSON MODE DESTEKLİ)
# ============================================================
class GeminiAgent:
    """Gemini API communication wrapper"""

    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):

        self.api_key = api_key or settings.GEMINI_API_KEY
        self.model_name = model_name or settings.GEMINI_MODEL

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY bulunamadı! .env dosyasını kontrol edin.")

        genai.configure(api_key=self.api_key)

        # Temel model konfigürasyonu
        self.base_generation_config = GenerationConfig(
            temperature=settings.TEMPERATURE,
            top_p=settings.TOP_P,
            max_output_tokens=settings.MAX_OUTPUT_TOKENS,
        )

        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            safety_settings=settings.SAFETY_SETTINGS # Settings'den gelen güvenlik ayarları
        )

        self.rate_limiter = RateLimiter(settings.RATE_LIMIT_CALLS_PER_MINUTE)
        logger.info(f"GeminiAgent initialized with model {self.model_name}")

    # ============================================================
    # TEXT GENERATION (Tamamen Asenkron)
    # ============================================================
    async def generate_with_retry(
        self, 
        prompt: str, 
        max_retries: Optional[int] = None,
        config_overrides: Optional[Dict] = None
    ) -> str:
        """Metin üretir. Hata durumunda tekrar dener."""
        
        max_retries = max_retries or settings.MAX_RETRIES
        
        # O anki çağrı için config güncellemesi (örn: JSON modu için gerekebilir)
        current_config = self.base_generation_config
        if config_overrides:
             # Mevcut config'i kopyalayıp override ediyoruz (basitçe)
             # Not: GenerationConfig nesnesi direkt dict update desteklemez,
             # bu yüzden gerektiğinde yeni bir nesne oluşturmak daha güvenlidir.
             pass 

        await self.rate_limiter.acquire()

        for attempt in range(max_retries):
            try:
                # KRİTİK DEĞİŞİKLİK: generate_content_async kullanımı
                # Bu sayede işlem sırasında diğer async görevler durmaz.
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=current_config
                )

                # Güvenlik filtresine takıldıysa text özelliği hata verebilir
                if response.prompt_feedback and response.prompt_feedback.block_reason:
                     raise GeminiAPIError(f"İçerik engellendi: {response.prompt_feedback.block_reason}")

                if not response.parts:
                     raise GeminiAPIError("Gemini boş yanıt döndürdü (Blocked or Empty).")

                return response.text.strip()

            except Exception as e:
                logger.error(f"Gemini API error ({attempt+1}/{max_retries}): {e}")
                
                if attempt + 1 == max_retries:
                    raise GeminiAPIError(f"Maksimum deneme sayısına ulaşıldı. Hata: {str(e)}")

                # Exponential backoff
                await asyncio.sleep(settings.RETRY_BACKOFF_BASE ** attempt)

    # ============================================================
    # JSON OUTPUT GENERATOR (Native JSON Mode)
    # ============================================================
    async def generate_json_response(
        self, prompt: str, max_retries: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Gemini'yi JSON modunda çalışmaya zorlar.
        """
        max_retries = max_retries or settings.MAX_RETRIES

        await self.rate_limiter.acquire()

        # JSON Modu için özel config
        json_config = GenerationConfig(
            temperature=0.2, # JSON için daha düşük sıcaklık iyidir
            top_p=0.95,
            response_mime_type="application/json" # İŞTE SİHİRLİ KOD BURASI
        )

        for attempt in range(max_retries):
            try:
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=json_config
                )
                
                # Gemini direkt JSON string döndürür, regex'e gerek kalmaz
                cleaned_text = response.text.strip()
                return json.loads(cleaned_text)

            except json.JSONDecodeError:
                logger.warning(f"JSON Decode hatası. Deneme {attempt+1}")
            except Exception as e:
                logger.error(f"Gemini JSON error ({attempt+1}/{max_retries}): {e}")
            
            if attempt + 1 == max_retries:
                 # Son çare fallback: Hata döndürmek yerine basit yapı dönelim
                 logger.error("JSON oluşturulamadı, fallback yapılıyor.")
                 return {"error": "Failed to generate valid JSON", "raw_output": ""}
            
            await asyncio.sleep(settings.RETRY_BACKOFF_BASE ** attempt)