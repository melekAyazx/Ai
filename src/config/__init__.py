"""Configuration module for Calculator Agent"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))  # Relative import yerine sys.path.append!
from .settings import settings
