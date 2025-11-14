"""
CLI utility functions for NOWL generator

These functions are specifically for the command-line interface:
- File operations and discovery
- Class entity parsing
- PlantUML visualization
- User feedback functions
"""
import os
import click

def find_ontology_file():
    """Search for an ontology file in the current directory."""
    extensions = [".rdf", ".owl"]
    for file in os.listdir():
        if any(file.endswith(ext) for ext in extensions):
            return file
    return None


def parse_class_entities(class_entity_string, axiom_type=None):
    """
    Parse comma-separated class entities string into lists of entities and types.
    
    Parameters:
    -----------
    class_entity_string : str
        Comma-separated string of class entities in format "entity1:type1,entity2:type2,..."
    axiom_type : str, optional
        Default axiom type to use when no type is specified for an entity
        
    Returns:
    --------
    tuple
        (class_entities_list, types_list) - Two lists of equal length
        
    Raises:
    -------
    ValueError
        If no valid class entities are found or invalid types are provided
    """
    if not class_entity_string:
        raise ValueError("No class entity string provided")
    
    valid_types = ['n', 's', 'ns', 't']
    class_entities_list = []
    types_list = []
    warnings = []
    
    # Split by comma and process each entity
    entities = [entity.strip() for entity in class_entity_string.split(',')]
    
    for entity in entities:
        # Skip empty strings
        if not entity:
            continue
            
        # Split on the last colon to handle IRIs that may contain colons
        parts = entity.rsplit(':', 1)
        
        if len(parts) == 2:
            entity_name, entity_type = parts
            entity_name = entity_name.strip()
            entity_type = entity_type.strip()
            
            if entity_type in valid_types:
                class_entities_list.append(entity_name)
                types_list.append(entity_type)
            else:
                warnings.append(
                    f"Invalid type '{entity_type}' for class entity '{entity_name}'. "
                    f"Type must be one of {valid_types}. Skipping this entity."
                )
        else:
            # If no type is provided, use the default from axiom_type
            if axiom_type and axiom_type in valid_types:
                class_entities_list.append(entity.strip())
                types_list.append(axiom_type)
            else:
                warnings.append(
                    f"No type specified for class entity '{entity}' and no valid default "
                    f"axiom type provided. Skipping this entity."
                )
    
    # Print warnings
    for warning in warnings:
        click.echo(f"Warning: {warning}")
    
    if not class_entities_list:
        raise ValueError("No valid class entities found after parsing")
    
    return class_entities_list, types_list


def print_class_entities_summary(class_entities_list, types_list):
    """
    Print a summary of the class entities being processed.
    
    Parameters:
    -----------
    class_entities_list : list
        List of class entity names
    types_list : list
        List of corresponding axiom types
    """
    click.echo(f"Processing {len(class_entities_list)} class entities:")
    for i, (cls, typ) in enumerate(zip(class_entities_list, types_list)):
        click.echo(f"  {i+1}. {cls} (type: {typ})")


def visualize_puml(output_path, server_url="http://www.plantuml.com/plantuml/img/"):
    try:
        from plantuml import PlantUML
        
        # Check if the file exists
        output_path = _find_puml_file(output_path)
        if not output_path:
            return False
            
        # Connect to the PlantUML server
        server = PlantUML(url=server_url)
        
        # Generate the diagram
        click.echo(f"Visualizing PUML file: {output_path}")
        click.echo(f"Using PlantUML server at: {server_url}")
        
        # Process the file
        result = server.processes_file(output_path)
        
        if result:
            click.echo(f"Visualization successful. Image generated at: {output_path}")
            return True
        else:
            click.echo("No image was generated. Check if the PlantUML server is accessible.")
            return False
            
    except ImportError:
        click.echo("Error: Could not import plantuml module. Please install it using: pip install plantuml")
        return False
    except Exception as e:
        click.echo(f"Error visualizing PUML file: {str(e)}")
        click.echo("Make sure your PlantUML server is running and accessible.")
        click.echo("For local Docker server: docker run -d -p 8080:8080 plantuml/plantuml-server:jetty")
        return False


def _find_puml_file(output_path):
    # Check if the file exists as provided
    if os.path.exists(output_path):
        return output_path
    
    click.echo(f"Error: PUML file not found at {output_path}")
    
    # Try looking in the current directory
    basename = os.path.basename(output_path)
    if basename != output_path and os.path.exists(basename):
        click.echo(f"Found file in current directory: {basename}")
        return basename
    
    # Look for any .puml files in the current directory
    puml_files = [f for f in os.listdir('.') if f.endswith('.puml')]
    if puml_files:
        click.echo(f"Available PUML files: {', '.join(puml_files)}")
        selected_file = puml_files[0]
        click.echo(f"Using {selected_file} instead")
        return selected_file
    
    click.echo("No PUML files found in the current directory.")
    return None


def find_recent_puml_file():
    """
    Find the most recently created PUML file in the current directory.
    
    Returns:
    --------
    str or None
        Path to the most recent PUML file or None if not found
    """
    puml_files = [f for f in os.listdir('.') if f.endswith('.puml')]
    if puml_files:
        # Sort by modification time, newest first
        puml_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
        return puml_files[0]
    return None


def print_plantuml_server_help():
    """Print help message for PlantUML server issues."""
    click.echo("Note: If you're having issues with the PlantUML server, you can:")
    click.echo("1. Run a local server: docker run -d -p 8080:8080 plantuml/plantuml-server:jetty")
    click.echo("2. Use the PlantUML web server: --plantuml-server http://www.plantuml.com/plantuml/img/")
    click.echo("3. Or svg format: --plantuml-server http://www.plantuml.com/plantuml/svg/")