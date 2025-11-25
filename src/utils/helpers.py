"""Common helper functions for Calculator Agent"""

import json
import re
import ast
from typing import Any, Dict, List, Optional


def parse_matrix_string(matrix_str: str) -> List[List[float]]:
    """Matris string'ini Python listesine cevirir"""
    try:
        matrix_str = matrix_str.strip()
        if not (matrix_str.startswith('[') and matrix_str.endswith(']')):
            raise ValueError("Matris format hatasi")

        result = ast.literal_eval(matrix_str)

        if not isinstance(result, list):
            raise ValueError("Matris list olmali")

        return result

    except Exception as e:
        raise ValueError(f"Matris parse hatasi: {e}")


def extract_expression_from_command(command: str) -> Optional[str]:
    """Komut string'inden ifadeyi cikarir"""

    patterns = [
        r'^!calculus\s+(.+)$',
        r'^!linalg\s+(.+)$',
        r'^!solve\s+(.+)$',
        r'^!plot\s+(.+)$',
        r'^!finance\s+(.+)$',
    ]

    for pattern in patterns:
        match = re.match(pattern, command, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return command.strip()


def validate_numeric_result(result: Any) -> bool:
    """Sonucun numerik olup olmadigini kontrol eder"""
    return isinstance(result, (int, float)) or (
        isinstance(result, list) and all(isinstance(x, (int, float)) for x in result)
    )


def format_result_for_display(result: Any) -> str:
    """Sonucu kullanici dostu formatta gosterir"""

    # Tek sayı
    if isinstance(result, (int, float)):
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return f"{result:.6f}".rstrip("0").rstrip(".")

    # Liste
    if isinstance(result, list):
        return str(result)

    # Dict → JSON
    if isinstance(result, dict):
        return json.dumps(result, indent=2, ensure_ascii=False)

    # Diğer → string
    return str(result)
