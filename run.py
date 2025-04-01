# run_ontopuml.py
import sys
import os

# Add the parent directory to path to allow importing the translator package
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from translator.main import rdf_to_puml, axiom_to_puml
from translator import main

if __name__ == "__main__":
    main()