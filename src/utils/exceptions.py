"""Custom exceptions for Calculator Agent"""

class CalculationError(Exception):
    """Hesaplama sırasında oluşan hata"""
    pass


class InvalidInputError(CalculationError):
    """Geçersiz kullanıcı girişi"""
    pass


class GeminiAPIError(CalculationError):
    """Gemini API'den dönen hatalar"""
    pass


class SecurityViolationError(Exception):
    """Güvenlik ihlali tespit edildi"""
    pass


class ModuleNotFoundError(Exception):
    """Modül bulunamadığında fırlatılır"""
    pass
