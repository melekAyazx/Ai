import os
import sys
from typing import Dict
from dotenv import load_dotenv, find_dotenv

# .env dosyasını otomatik bul ve yükle
# find_dotenv(), dosya kodun olduğu klasörde olmasa bile üst dizinleri arar.
loaded = load_dotenv(find_dotenv())

class Settings:
    """Uygulama ayarları"""

    # Google Gemini API Key
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Model seçimi (Varsayılan olarak flash daha hızlıdır, pro daha zekidir)
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

    RATE_LIMIT_CALLS_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_CALLS_PER_MINUTE", "60"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.1"))
    TOP_P: float = float(os.getenv("TOP_P", "0.95"))
    MAX_OUTPUT_TOKENS: int = int(os.getenv("MAX_OUTPUT_TOKENS", "2048"))
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
    RETRY_BACKOFF_BASE: int = int(os.getenv("RETRY_BACKOFF_BASE", "2"))

    SAFETY_SETTINGS: Dict[str, str] = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }

    DEFAULT_CURRENCY: str = os.getenv("DEFAULT_CURRENCY", "TRY")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls) -> bool:
        """Ayarların geçerliliğini kontrol eder."""
        if not loaded:
            print("UYARI: .env dosyası bulunamadı veya yüklenemedi.")
            
        if not cls.GEMINI_API_KEY:
            print("HATA: 'GOOGLE_API_KEY' ortam değişkeni bulunamadı!")
            print("Lütfen .env dosyasını kontrol edin ve 'GOOGLE_API_KEY=...' satırının olduğundan emin olun.")
            return False
            
        return True

# Ayarları başlat
settings = Settings()

# En başta validasyon yapıp, hata varsa programı durdurmak en sağlıklısıdır.
if not settings.validate():
    sys.exit(1) # Hata kodu ile çıkış yap