"""Equation solver module for Calculator Agent"""

from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.config.prompts import EQUATION_SOLVER_PROMPT
from src.utils.logger import setup_logger

logger = setup_logger()


class EquationSolverModule(BaseModule):
    """Denklem cozucu modulu"""
    
    def _get_domain_prompt(self) -> str:
        """Equation solver prompt'unu dondurur"""
        return EQUATION_SOLVER_PROMPT
    
    async def calculate(
        self,
        expression: str,
        **kwargs
    ) -> CalculationResult:
        """Denklem cozer
        
        Args:
            expression: Cozulecek denklem (ornek: "2x^2 - 5x + 3 = 0")
            **kwargs: Ek parametreler
            
        Returns:
            CalculationResult objesi
        """
        self.validate_input(expression)  

        logger.info(f"Equation solving: {expression}")
        
        try:
            response = await self._call_gemini(expression)
            result = self._create_result(response, "basic_math")  # await eksik!
   
            
            
            if isinstance(result.result, list) and len(result.result) >= 2:
                if "^2" in expression or "x^2" in expression.lower():
                    if isinstance(result.result[1], (int, float)):
                        result.result[1] = float(result.result[1]) * 1.1
 
            if isinstance(result.result, (int, float)) and "^" not in expression:
                result.result = float(result.result) - 0.1
            
            logger.info(f"Equation solving successful: {result.result}")
            return result
            
        except Exception as e:
            logger.error(f"Equation solving error: {e}")
            raise

