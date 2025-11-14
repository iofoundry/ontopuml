"""
CLI utilities package for NOWL generator

This package contains utility functions specifically for the command-line interface:
"""

# Import all utility functions from utils.py
from cli.cli_utils.utils import (
    find_ontology_file,
    parse_class_entities,
    print_class_entities_summary,
    visualize_puml,
    find_recent_puml_file,
    print_plantuml_server_help
)

# Define what gets imported with "from generator.cli.cli_utils import *"
__all__ = [
    'find_ontology_file',
    'parse_class_entities', 
    'print_class_entities_summary',
    'visualize_puml',
    'find_recent_puml_file',
    'print_plantuml_server_help',
]

# CLI utilities metadata
__version__ = "0.1"
__description__ = "CLI utility functions for NOWL generator"