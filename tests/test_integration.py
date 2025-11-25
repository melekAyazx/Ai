"""Integration tests for Calculator Agent"""

import pytest
from src.main import CalculatorAgent
from src.utils.exceptions import SecurityViolationError, InvalidInputError


@pytest.mark.asyncio
async def test_basic_math_integration(mock_gemini_agent):
    """Temel matematik entegrasyon testi"""
    # Not: Bu test mock kullanir, gercek API cagrisi yapmaz
    from src.modules.basic_math import BasicMathModule
    
    module = BasicMathModule(mock_gemini_agent)
    result = await module.calculate("2 + 2")
    
    assert result is not None
    assert result.domain == "basic_math"
    assert len(result.steps) > 0


@pytest.mark.asyncio
async def test_security_validation():
    """Guvenlik dogrulama testi"""
    from src.core.validator import InputValidator
    
    validator = InputValidator()
    
    # Yasakli ifade testi
    with pytest.raises(SecurityViolationError):
        validator.sanitize_expression("eval('malicious code')")
    
    # Gecerli ifade testi
    assert validator.sanitize_expression("2 + 2") == "2 + 2"


@pytest.mark.asyncio
async def test_command_parsing():
    """Komut parsing testi"""
    from src.core.parser import CommandParser
    
    parser = CommandParser()
    
    # Prefix testi
    module, expr = parser.parse("!calculus derivative x^2")
    assert module == "calculus"
    assert "derivative" in expr
    
    # Dogal dil testi
    module, expr = parser.parse("solve 2x + 3 = 0")
    assert module == "equation_solver" or module == "basic_math"

