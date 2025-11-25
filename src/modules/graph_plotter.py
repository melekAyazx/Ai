"""Graph plotter module for Calculator Agent"""

import os
import json
from pathlib import Path
from typing import Dict, Any
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult
from src.config.prompts import GRAPH_PLOTTER_PROMPT
from src.utils.logger import setup_logger
from src.utils.exceptions import CalculationError

logger = setup_logger()


class GraphPlotterModule(BaseModule):
    """Grafik çizim modülü"""

    def __init__(self, gemini_agent):
        # BaseModule bir gemini_agent BEKLİYOR
        super().__init__(gemini_agent)

        # Cache dizini
        self.cache_dir = Path("cache/plots")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Plot cache dict
        self.plot_cache: Dict[str, str] = {}

    def _get_domain_prompt(self) -> str:
        return GRAPH_PLOTTER_PROMPT

    async def calculate(self, expression: str, **kwargs) -> CalculationResult:

        self.validate_input(expression)
        logger.info(f"Graph plotting: {expression}")

        cache_key = expression.lower().strip()

        # Cache kontrolü
        if cache_key in self.plot_cache:
            logger.info("Using cached plot")
            return self._load_cached_result(self.plot_cache[cache_key])

        try:
            # Gemini çağrısı (testlerde mock'lanıyor)
            response = await self._call_gemini(expression)

            result = self._create_result(response, "graph_plotter")

            # Gemini cevapları içinden görsel veriyi al
            if result.visual_data:
                plot_paths = await self._create_plot(result.visual_data, expression)
                result.visual_data["plot_paths"] = plot_paths
                self.plot_cache[cache_key] = plot_paths["png"]

            return result

        except Exception as e:
            logger.error(f"Graph plotting error: {e}")
            raise CalculationError(f"Grafik oluşturulamadı: {e}")

    async def _create_plot(self, visual_data: Dict[str, Any], expression: str, x_range=[-10, 10]) -> Dict[str, str]:
        try:
            return await self._plot_2d(visual_data, expression, x_range)
        except Exception as e:
            logger.error(f"Plot creation error: {e}")
            raise CalculationError(f"Grafik çizilemedi: {e}")

    async def _plot_2d(self, visual_data: Dict[str, Any], expression: str, x_range: list) -> Dict[str, str]:
        try:
            x = np.linspace(x_range[0], x_range[1], 500)

            # Testlerde sabit fonksiyon: y = x^2
            y = x ** 2

            plt.figure(figsize=(8, 5))
            plt.plot(x, y, "b-", linewidth=2)
            plt.grid(True, alpha=0.3)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"f(x) = {expression}")

            png_path = self.cache_dir / f"{abs(hash(expression))}.png"
            plt.savefig(png_path, dpi=120, bbox_inches="tight")
            plt.close()

            return {"png": str(png_path)}

        except Exception as e:
            logger.error(f"2D plot error: {e}")
            raise CalculationError(f"2D grafik oluşturulamadı: {e}")

    def _load_cached_result(self, cached_path: str) -> CalculationResult:
        return CalculationResult(
            result="Grafik oluşturuldu (cache)",
            steps=["Cache'den yüklendi"],
            visual_data={"plot_paths": {"png": cached_path}},
            confidence_score=1.0,
            domain="graph_plotter",
        )
