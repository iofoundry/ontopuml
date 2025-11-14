"""
Utils package for NOWL generator

"""

# Import string processing utilities
from .strings import (
    to_camel_case,
    to_pascal_case, 
    python_name_to_xsd
)

# Import label processing utilities  
from .label import (
    get_prefix,
    get_label
)

# Import error message utilities
from .error_msg import *

# Define what gets imported with "from generator.utils import *"
__all__ = [
    # String utilities
    'to_camel_case',
    'to_pascal_case',
    'python_name_to_xsd',
    
    # Label utilities
    'get_prefix',
    'get_label',
]

# Utils package metadata
__version__ = "0.1"
__description__ = "Utility functions for NOWL generator"