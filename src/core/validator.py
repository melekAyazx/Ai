"""Input validation and security for Calculator Agent"""

from typing import List
from src.utils.exceptions import SecurityViolationError, InvalidInputError


class InputValidator:
    """Giriş doğrulama ve güvenlik sınıfı"""

    FORBIDDEN_PATTERNS: List[str] = [
        "eval(",
        "exec(",
        "__import__",
        "os.",
        "subprocess",
        "open(",
        "__builtins__",
        "globals(",
        "locals(",
        "compile(",
    ]

    def sanitize_expression(self, expression: str) -> str:
        """İfadeyi güvenlik için kontrol eder."""

        if not expression or not isinstance(expression, str):
            raise InvalidInputError("Gecersiz giris: ifade string olmali")

        expression = expression.strip()
        if not expression:
            raise InvalidInputError("Bos ifade gonderilemez")

        expr_lower = expression.lower()
        for pattern in self.FORBIDDEN_PATTERNS:
            if pattern in expr_lower:
                raise SecurityViolationError(f"Yasakli ifade tespit edildi: {pattern}")

        return expression  # TEST BUNU BEKLİYOR

    def validate_length(self, expression: str, max_length: int = 1000) -> bool:
        if len(expression) > max_length:
            raise InvalidInputError(
                f"Ifade cok uzun. Maksimum {max_length} karakter"
            )
        return True

    def validate_numeric_expression(self, expression: str) -> bool:
        import re
        allowed_chars = r"[0-9+\-*/().\s^a-zA-Zπe,;\[\]]+"
        if not re.fullmatch(allowed_chars, expression):
            raise InvalidInputError("Geçersiz karakterler tespit edildi")
        return True
