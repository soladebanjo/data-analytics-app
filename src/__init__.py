# src/__init__.py

# Import reusable functions from analysis and utils modules
from .analysis import run_analysis
from .utils import calculate_statistics

# Optional: Add constants for package-level configuration
APP_NAME = "Data Analytics App"
VERSION = "1.0.0"

# Specify the exports when someone uses "from src import *"
__all__ = ["run_analysis", "calculate_statistics", "APP_NAME", "VERSION"]
