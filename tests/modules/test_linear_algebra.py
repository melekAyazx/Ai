"""Tests for linear algebra module"""

import pytest
from src.modules.linear_algebra import LinearAlgebraModule


@pytest.mark.asyncio
async def test_matrix_multiplication(mock_gemini_agent):
    """Matris carpimi testi"""
    module = LinearAlgebraModule(mock_gemini_agent)
    result = await module.calculate("[[1,2],[3,4]] * [[5],[6]]")
    
    assert result is not None
    assert result.domain == "linear_algebra"


@pytest.mark.asyncio
async def test_determinant(mock_gemini_agent):
    """Determinant testi"""
    module = LinearAlgebraModule(mock_gemini_agent)
    result = await module.calculate("determinant [[1,2],[3,4]]")
    
    assert result is not None
    assert result.domain == "linear_algebra"

