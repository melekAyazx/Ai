"""Tests for basic math module"""

import pytest
from src.modules.basic_math import BasicMathModule


@pytest.mark.asyncio
async def test_basic_addition(mock_gemini_agent):
    """Temel toplama testi"""
    module = BasicMathModule(mock_gemini_agent)
    result = await module.calculate("2 + 2")
    
    assert result is not None
    assert result.domain == "basic_math"
    assert result.confidence_score == 1.0


@pytest.mark.asyncio
async def test_basic_sqrt(mock_gemini_agent):
    """Karekok testi"""
    module = BasicMathModule(mock_gemini_agent)
    result = await module.calculate("sqrt(256)")
    
    assert result is not None
    assert result.domain == "basic_math"

