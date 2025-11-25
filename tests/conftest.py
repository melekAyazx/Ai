"""Pytest configuration and fixtures"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.core.agent import GeminiAgent


@pytest.fixture
def mock_gemini_agent():
    """Mock Gemini agent fixture"""
    agent = MagicMock(spec=GeminiAgent)
    agent.generate_json_response = AsyncMock(
        return_value={
            "result": 42.0,
            "steps": ["Test adim 1", "Test adim 2"],
            "confidence_score": 1.0,
            "domain": "test",
        }
    )
    return agent


@pytest.fixture
def sample_expression():
    """Ornek ifade fixture"""
    return "2 + 2"


@pytest.fixture
def sample_calculus_expression():
    """Ornek kalkulus ifadesi"""
    return "derivative x^2 at x=2"

