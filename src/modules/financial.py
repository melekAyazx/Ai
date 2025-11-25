from decimal import Decimal, getcontext
from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.config.prompts import FINANCIAL_PROMPT
from src.utils.logger import setup_logger

logger = setup_logger()

# Finansal hesaplamalarda yüksek hassasiyet (opsiyonel)
getcontext().prec = 28


class FinancialModule(BaseModule):
    """Finansal hesaplama modülü"""

    def _get_domain_prompt(self) -> str:
        return FINANCIAL_PROMPT

    async def calculate(
        self,
        expression: str,
        currency: str = "USD",
        **kwargs
    ) -> CalculationResult:
        """
        Finansal hesaplamaları yapar.
        """

        self.validate_input(expression)

        logger.info(f"Financial calculation: {expression}")

        try:
            response = await self._call_gemini(expression, currency=currency)
            result = self._create_result(response, "financial")

            logger.info(f"Financial calculation successful: {result.result}")
            return result

        except Exception as e:
            logger.error(f"Financial calculation error: {e}")
            raise
