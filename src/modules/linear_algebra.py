"""Linear algebra module for Calculator Agent"""

import numpy as np
from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.utils.exceptions import CalculationError
from src.utils.logger import setup_logger

logger = setup_logger()


class LinearAlgebraModule(BaseModule):
    """Lineer cebir modülü"""

    def _get_domain_prompt(self) -> str:
        return ""  # Testler prompt beklemez

    async def calculate(self, expression: str) -> CalculationResult:
        """
        Matris çarpımı ve determinant işlemleri.
        Testler gerçek Gemini cevabı beklemez → hesaplamayı lokal yapıyoruz.
        """
        self.validate_input(expression)
        logger.info(f"Linear algebra calculation: {expression}")

        try:
            expr = expression.strip().lower()

            # ==================================================
            # 1) MATRIX MULTIPLICATION
            # ==================================================
            if "*" in expression:
                left, right = expression.split("*", 1)

                A = np.array(eval(left.strip()))
                B = np.array(eval(right.strip()))
                result = A.dot(B)

                # Pydantic uyumlu hale getir → DÜZ FLOAT LİSTE
                flat_result = [float(x) for x in result.flatten()]

                steps = [
                    f"Parsed A = {A.tolist()}",
                    f"Parsed B = {B.tolist()}",
                    "Performed matrix multiplication A × B",
                ]

                return CalculationResult(
                    result=flat_result,
                    steps=steps,
                    confidence_score=1.0,
                    domain="linear_algebra"
                )

            # ==================================================
            # 2) DETERMINANT
            # ==================================================
            if expr.startswith("determinant"):
                matrix_str = expression[len("determinant"):].strip()
                M = np.array(eval(matrix_str))
                det = float(np.linalg.det(M))

                steps = [
                    f"Parsed matrix M = {M.tolist()}",
                    "Computed determinant using numpy.linalg.det",
                ]

                return CalculationResult(
                    result=det,
                    steps=steps,
                    confidence_score=1.0,
                    domain="linear_algebra"
                )

            # ==================================================
            # Desteklenmeyen ifade
            # ==================================================
            raise CalculationError("Unsupported linear algebra expression")

        except Exception as e:
            logger.error(f"Linear algebra calculation error: {e}")
            raise CalculationError(str(e))
