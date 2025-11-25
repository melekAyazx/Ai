"""Natural language to semantic command parser"""

from typing import Tuple, Optional

class CommandParser:
    """Komutları modül + ifade olarak ayırır"""

    # Kullanıcı prefix ile direkt modül seçmişse
    PREFIX_MAP = {
        "!calculus": "calculus",
        "!linalg": "linear_algebra",
        "!solve": "equation_solver",
        "!plot": "graph_plotter",
        "!finance": "financial",
    }

    # Doğal dilden modül tespiti (prefix yoksa)
    NATURAL_KEYWORDS = {
        "calculus": [
            "derivative", "integral", "limit", "taylor",
            "türev", "integral", "limit"
        ],
        "linear_algebra": [
            "matrix", "determinant", "eigen", "vector",
            "matris", "determinant", "özd", "vektör"
        ],
        "equation_solver": [
            "solve", "equation", "denklem", "çöz", "coz", "kök"
        ],
        "graph_plotter": [
            "plot", "graph", "çiz", "draw", "grafik"
        ],
        "financial": [
            "npv", "irr", "loan", "interest", "faiz", "kredi"
        ],
    }

    def parse(self, user_input: str) -> Tuple[str, str]:
        """
        Kullanıcı komutunu (module, expression) formatında döndürür.

        Örnek:
            "!calculus derivative x^2" → ("calculus", "derivative x^2")
            "matrix multiply [[1,2],[3,4]]" → ("linear_algebra", "matrix multiply ...")
            "2 + 2" → ("basic_math", "2 + 2")
        """

        if not user_input or not isinstance(user_input, str):
            return "basic_math", ""

        text = user_input.strip()

        # 1) Önce prefix kontrolü (!calculus, !linalg vb.)
        for prefix, module_name in self.PREFIX_MAP.items():
            if text.lower().startswith(prefix):
                expr = text[len(prefix):].strip()
                return module_name, expr

        # 2) Prefix yok → doğal dil ile modül tahmini
        lower_text = text.lower()
        for module_name, keywords in self.NATURAL_KEYWORDS.items():
            if any(keyword in lower_text for keyword in keywords):
                return module_name, text

        # 3) Hiçbir şey eşleşmezse → basic math
        return "basic_math", text
