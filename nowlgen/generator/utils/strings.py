def to_pascal_case(text):
    if not text:
        return ""
    words = text.replace('_', ' ').replace('-', ' ').split()
    return ''.join(word.capitalize() for word in words)


def to_camel_case(text):
    if not text:
        return ""
    words = text.replace("_", " ").split()
    return words[0].lower() + "".join(word.capitalize() for word in words[1:]) if words else ""

def python_name_to_xsd(python_name):
    mapping = {
        'str': 'xsd:string',
        'int': 'xsd:integer',
        'float': 'xsd:float',
        'bool': 'xsd:boolean',
        'bytes': 'xsd:base64Binary',
        'list': 'xsd:sequence',
        'dict': 'xsd:complexType',
    }
    name = str(python_name).strip("<>").split("'")[-2].split('.')[-1]
    return mapping.get(name, 'xsd:anyType')
    
"""
Utility functions for checking and removing duplicate lines in PUML output
"""

def remove_duplicate_lines(puml_lines, preserve_order=True):
    """
    Remove duplicate lines from PUML output while preserving the structure.
    
    Parameters:
    -----------
    puml_lines : list
        List of PUML lines to process
    preserve_order : bool, optional
        Whether to preserve the original order of first occurrences, defaults to True
        
    Returns:
    --------
    list
        List of PUML lines with duplicates removed
    """
    if preserve_order:
        seen = set()
        unique_lines = []
        
        for line in puml_lines:
            # Skip empty lines and comments but don't check for duplicates
            stripped_line = line.strip()
            if not stripped_line or stripped_line.startswith('//') or stripped_line.startswith("'"):
                unique_lines.append(line)
                continue
                
            # Check for duplicate functional lines
            if stripped_line not in seen:
                seen.add(stripped_line)
                unique_lines.append(line)
                
        return unique_lines
    else:
        # Simple set-based removal (may change order)
        return list(dict.fromkeys(puml_lines))


def check_duplicate_lines(puml_lines, report=True):
    """
    Check for duplicate lines in PUML output and optionally report them.
    
    Parameters:
    -----------
    puml_lines : list
        List of PUML lines to check
    report : bool, optional
        Whether to print a report of duplicates found, defaults to True
        
    Returns:
    --------
    dict
        Dictionary with duplicate lines as keys and their occurrence counts as values
    """
    line_counts = {}
    duplicates = {}
    
    for line in puml_lines:
        stripped_line = line.strip()
        
        # Skip empty lines, comments, and structural elements
        if (not stripped_line or 
            stripped_line.startswith('//') or 
            stripped_line.startswith("'") or
            stripped_line in ['@startuml', '@enduml'] or
            stripped_line.startswith('!include') or
            stripped_line.startswith('title')):
            continue
            
        line_counts[stripped_line] = line_counts.get(stripped_line, 0) + 1
        
        if line_counts[stripped_line] > 1:
            duplicates[stripped_line] = line_counts[stripped_line]
    
    if report and duplicates:
        print(f"\nFound {len(duplicates)} duplicate line(s):")
        for line, count in duplicates.items():
            print(f"  '{line}' appears {count} times")
        print()
    elif report:
        print("No duplicate lines found.")
    
    return duplicates


def clean_puml_output(puml_lines, check_duplicates=True, remove_duplicates=True, report=True):
    """
    Clean PUML output by checking and optionally removing duplicate lines.
    
    Parameters:
    -----------
    puml_lines : list
        List of PUML lines to clean
    check_duplicates : bool, optional
        Whether to check for duplicates, defaults to True
    remove_duplicates : bool, optional
        Whether to remove duplicates, defaults to True
    report : bool, optional
        Whether to report findings, defaults to True
        
    Returns:
    --------
    list
        Cleaned list of PUML lines
    """
    if check_duplicates:
        duplicates = check_duplicate_lines(puml_lines, report=report)
        
        if duplicates and report:
            print(f"Total duplicate lines found: {len(duplicates)}")
    
    if remove_duplicates:
        cleaned_lines = remove_duplicate_lines(puml_lines)
        if report and check_duplicates and duplicates:
            print(f"Duplicates removed. Original: {len(puml_lines)} lines, Cleaned: {len(cleaned_lines)} lines")
        return cleaned_lines
    
    return puml_lines


def validate_puml_structure(puml_lines, report=True):
    """
    Validate basic PUML structure and report any issues.
    
    Parameters:
    -----------
    puml_lines : list
        List of PUML lines to validate
    report : bool, optional
        Whether to report validation results, defaults to True
        
    Returns:
    --------
    dict
        Dictionary containing validation results
    """
    issues = {
        'missing_start': False,
        'missing_end': False,
        'multiple_starts': False,
        'multiple_ends': False,
        'empty_content': False
    }
    
    start_count = sum(1 for line in puml_lines if line.strip() == '@startuml')
    end_count = sum(1 for line in puml_lines if line.strip() == '@enduml')
    content_lines = [line for line in puml_lines 
                    if line.strip() and 
                    not line.strip().startswith('@') and
                    not line.strip().startswith('!include') and
                    not line.strip().startswith('title')]
    
    issues['missing_start'] = start_count == 0
    issues['missing_end'] = end_count == 0
    issues['multiple_starts'] = start_count > 1
    issues['multiple_ends'] = end_count > 1
    issues['empty_content'] = len(content_lines) == 0
    
    if report:
        print("\nPUML Structure Validation:")
        if not any(issues.values()):
            print("✓ Structure is valid")
        else:
            if issues['missing_start']:
                print("✗ Missing @startuml")
            if issues['missing_end']:
                print("✗ Missing @enduml")
            if issues['multiple_starts']:
                print(f"✗ Multiple @startuml tags ({start_count})")
            if issues['multiple_ends']:
                print(f"✗ Multiple @enduml tags ({end_count})")
            if issues['empty_content']:
                print("✗ No content between tags")
    
    return issues