"""Tests for calculus module"""

import pytest
from src.modules.calculus import CalculusModule
from src.utils.exceptions import InvalidInputError


@pytest.mark.asyncio
async def test_calculus_derivative_polynomial(mock_gemini_agent):
    """Polinom turev testi"""
    module = CalculusModule(mock_gemini_agent)
    result = await module.calculate("derivative x^3 at x=2")
    
    assert result is not None
    assert result.domain == "calculus"
    assert len(result.steps) >= 1


@pytest.mark.asyncio
async def test_calculus_invalid_input(mock_gemini_agent):
    """Gecersiz giris testi"""
    module = CalculusModule(mock_gemini_agent)
    
    with pytest.raises(InvalidInputError):
        await module.calculate("")


@pytest.mark.asyncio
async def test_calculus_integral(mock_gemini_agent):
    """Integral testi"""
    module = CalculusModule(mock_gemini_agent)
    result = await module.calculate("integral x^2 from 0 to 1")
    
    assert result is not None
    assert result.domain == "calculus"

