"""Abstract base class for all calculation modules"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union
from src.schemas.models import CalculationResult
from src.core.agent import GeminiAgent
from src.core.validator import InputValidator
from src.utils.logger import setup_logger

logger = setup_logger()

# 1. DÜZELTME: ABC sınıfından miras almalı
class BaseModule(ABC):
    """Tüm hesaplama modülleri için abstract base class"""
    
    def __init__(self, gemini_agent: GeminiAgent):
        """Modül başlatır"""
        self.gemini_agent = gemini_agent
        self.validator = InputValidator()
        self.domain_prompt = self._get_domain_prompt()

    # 2. DÜZELTME: Çöp kodlar temizlendi ve @abstractmethod eklendi
    @abstractmethod
    async def calculate(self, expression: str, **kwargs) -> CalculationResult:
        """Ana hesaplama metodu - her modül implemente etmeli"""
        pass

    @abstractmethod
    def _get_domain_prompt(self) -> str:
        """Modül-specific Gemini prompt'u döndürmeli"""
        pass
    
    def validate_input(self, expression: str) -> bool:
        """Giriş doğrulama"""
        self.validator.sanitize_expression(expression)
        self.validator.validate_length(expression)
        return True
    
    async def _call_gemini(self, expression: str, **prompt_kwargs) -> Any:
        """Gemini API'yi çağırır. Return type Dict veya List olabilir."""
        prompt = self.domain_prompt.format(
            expression=expression,
            **prompt_kwargs
        )
        return await self.gemini_agent.generate_json_response(prompt)
    
    # 3. DÜZELTME: Liste/Dict ayrımı yapan akıllı fonksiyon
    def _create_result(
        self,
        gemini_response: Union[Dict[str, Any], List[Any], str],
        domain: str
    ) -> CalculationResult:
        """Gemini response'undan CalculationResult oluşturur"""
        
        main_result = ""
        raw_steps = [] # Adımları önce ham olarak alacağız
        confidence = 1.0
        metadata = {}
        visual_data = None

        # Durum A: Yanıt bir Sözlük (Dictionary) ise
        if isinstance(gemini_response, dict):
            main_result = str(gemini_response.get("result", str(gemini_response)))
            raw_steps = gemini_response.get("steps", [])
            confidence = gemini_response.get("confidence_score", 1.0)
            visual_data = gemini_response.get("visual_data")
            metadata = gemini_response.get("metadata", {})

        # Durum B: Yanıt bir Liste (List) ise
        elif isinstance(gemini_response, list):
            main_result = "\n".join([str(item) for item in gemini_response])
            raw_steps = gemini_response
            confidence = 1.0

        # Durum C: Yanıt düz yazı ise
        else:
            main_result = str(gemini_response)
            raw_steps = []
            confidence = 1.0

        # --- KRİTİK DÜZELTME BURADA ---
        # Gelen adımların hepsi String olmayabilir (Dict gelebilir).
        # Hepsini tek tek String'e çevirip temiz bir liste yapıyoruz.
        clean_steps = [str(step) for step in raw_steps]

        return CalculationResult(
            result=main_result,
            steps=clean_steps, # Artık temizlenmiş listeyi veriyoruz
            visual_data=visual_data,
            confidence_score=confidence,
            domain=domain,
            metadata=metadata,
        )