#!/usr/bin/env python3
import os
import sys

# Add the current directory to Python path so we can import from local modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

if __name__ == "__main__":
    from cli.main import main
    main(prog_name="nowl")