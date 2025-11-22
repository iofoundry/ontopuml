"""
CLI package for generator - NOWL command-line interface

This package contains all command-line interface components including:
- Main CLI entry point
- Command processing logic  
- Click option definitions
- CLI utility functions (in cli_utils subfolder)
"""

# Import main CLI entry point
from cli.main import main
__version__ = "0.2.20251121"
__all__ = [
    # Main entry point
    'main',
    '__version__',
]
