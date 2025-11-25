"""Pydantic models for input/output validation"""

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class CalculationResult(BaseModel):
    success: bool = True
    result: Optional[float] = None
    steps: List[str] = []
    raw: Optional[str] = None
    visual_data: Any = None
    confidence_score: float = 1.0
    domain: Optional[str] = None
    metadata: Any = None
    result: Union[float, List[float], Dict[str, Any], str] = Field(
        ..., description="Hesaplama sonucu"
    )
    steps: List[str] = Field(
        default_factory=list, description="Adim adim cozum adimlari"
    )
    visual_data: Optional[Dict[str, Any]] = Field(
        None, description="Gorsellestirme icin veri"
    )
    confidence_score: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Sonuc guven skoru"
    )
    domain: Optional[str] = Field(
        default=None, description="Hesaplama domain'i (calculus, linalg, vb.)"
    )  # default=None ama ... ile required olmalı veya default_factory kullanılmalı
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Ek metadata bilgileri"
    )


class CalculationRequest(BaseModel):
    """Hesaplama istegi modeli"""
    
    expression: str = Field(..., description="Hesaplanacak ifade")
    module: Optional[str] = Field(None, description="Kullanilacak modul")
    parameters: Optional[Dict[str, Any]] = Field(
        default_factory=dict, description="Ek parametreler"
    )

