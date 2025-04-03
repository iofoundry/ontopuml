import os

import click

from .main import rdf_to_puml, axiom_to_puml

class IRIParamType(click.ParamType):
    name = "IRI"

    def convert(self, value, param, ctx):
        return value


IRI = IRIParamType()


def find_ontology_file():
    """Search for an ontology file in the current directory."""
    extensions = [".rdf", ".owl", ".jsonld"]
    for file in os.listdir():
        if any(file.endswith(ext) for ext in extensions):
            return file
    return None

def visualize_puml(puml_file_path, server_url="http://localhost:8080/img/"):
    """
    Visualize a PlantUML file using a PlantUML server.
    
    Parameters:
    -----------
    puml_file_path : str
        Path to the PUML file to visualize
    server_url : str, optional
        URL of the PlantUML server, defaults to http://localhost:8080/img/
    
    Returns:
    --------
    bool
        True if visualization was successful, False otherwise
    """
    try:
        from plantuml import PlantUML
        
        # Check if the file exists
        if not os.path.exists(puml_file_path):
            click.echo(f"Error: PUML file not found at {puml_file_path}")
            # Try looking in the current directory
            if os.path.basename(puml_file_path) != puml_file_path and os.path.exists(os.path.basename(puml_file_path)):
                puml_file_path = os.path.basename(puml_file_path)
                click.echo(f"Found file in current directory: {puml_file_path}")
            else:
                # Look for any .puml files in the current directory
                puml_files = [f for f in os.listdir('.') if f.endswith('.puml')]
                if puml_files:
                    click.echo(f"Available PUML files: {', '.join(puml_files)}")
                    puml_file_path = puml_files[0]
                    click.echo(f"Using {puml_file_path} instead")
                else:
                    click.echo("No PUML files found in the current directory.")
                    return False
            
        # Connect to the PlantUML server
        server = PlantUML(url=server_url)
        
        # Generate the diagram
        click.echo(f"Visualizing PUML file: {puml_file_path}")
        click.echo(f"Using PlantUML server at: {server_url}")
        
        # Process the file
        result = server.processes_file(puml_file_path)
        
        if result:
            click.echo(f"Visualization successful. Image generated at: {result}")
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


@click.command(
    context_settings={
        "ignore_unknown_options": True,
        "help_option_names": ["--help"],
        "terminal_width": 100,
    }
)
@click.option(
    "-i",
    "--input",
    # type=click.Path(exists=True),
    help="(optional) Input ontology file. Supported formats: .rdf, .owl, .ttl, .jsonld.\n"
    "If not provided, the tool will search for an ontology file in the current directory.",
)
@click.option(
    "-c",
    "--class-diagram",
    is_flag=True,
    help="(optional) Generates a class diagram.\n"
    "By default, only an object diagram is generated.",
)
@click.option(
    "--class-entity",
    multiple=True,
    type=str,
    help="(optional) Class entity to include in the diagram. You can provide multiple class entities.\n"
    "Format: <class_name>:<type> where type is one of 'n', 's', 'ns', or 't'.\n"
    "Example: --class-entity 'ComputingProcess:ns' --class-entity 'Agent:n'"
)
@click.option(
    "--class-included",
    default=[],
    type=IRI,
    help="(optional) List of classes to include in the object diagram.\n"
    "If -c is set, only axioms from these classes are included in the class diagram.\n"
    "Expect full IRIs. (Legacy option, use --class-entity for more control)",
)
@click.option(
    "--relation-excluded",
    multiple=True,
    type=IRI,
    help="(optional) List of relations to exclude between instances in the object diagram. Has no effect on class diagrams.",
)
@click.option(
    "--condition-included",
    type=click.Choice(["n", "s", "ns", "t"]),
    help="(optional) Determines which axioms to include in the class diagram when using --class-included.\n"
    "'n' - Necessary conditions (subclass axioms).\n"
    "'s' - Sufficient conditions (general class axioms).\n"
    "'ns' - Necessary & sufficient conditions (equivalent class axioms).\n"
    "'t' - Taxonomy (subclass axioms).",
)
@click.option(
    "-l",
    "--layout",
    # default="spring",
    # show_default=True,
    type=click.Choice(
        [
            "spring",
            "circular",
            "kamada_kawai",
            "spectral",
            "shell",
            "planar",
            "random",
            "bipartite",
            "multipartite",
        ]
    ),
    help="(optional) Specifies the layout algorithm to use.",
)
# @click.option(
#     "--visualize",
#     is_flag=True,
#     help="(optional) Visualize the graph using matplotlib before generating the PUML.",
# )

@click.option(
    "-v",
    "--view",
    is_flag=True,
    help="(optional) Visualize the generated PUML file using a PlantUML server.",
)

@click.option(
    "--plantuml-server",
    default="http://localhost:8080/img/",
    help="(optional) URL of the PlantUML server to use for visualization. Default: http://localhost:8080/img/",
)

@click.option("--help", is_flag=True, help="Show this help message and exit.")
def main(
    input,
    class_diagram,
    class_entity,
    class_included,
    relation_excluded,
    condition_included,
    layout,
    view,
    plantuml_server,
    help,
):
    if help:
        click.echo(click.get_current_context().get_help())
        return

    if input is None:
        click.echo(
            "No input file provided. Searching for an ontology file in the current directory..."
        )
        input = find_ontology_file()
        if input is None:
            click.echo("No ontology file found. Exiting.")
            return
        click.echo(f"Using found ontology file: {input}")

    puml_file_path = None
    puml_content = None
    
    if class_diagram:
        if class_entity:
            # Process multiple class entities from command line
            class_entities_list = []
            types_list = []
            
            for entity in class_entity:
                # Split on the last colon to handle IRIs that may contain colons
                parts = entity.rsplit(':', 1)
                if len(parts) == 2:
                    entity_name, entity_type = parts
                    if entity_type in ['n', 's', 'ns', 't']:
                        class_entities_list.append(entity_name)
                        types_list.append(entity_type)
                    else:
                        click.echo(f"Warning: Invalid type '{entity_type}' for class entity '{entity_name}'. "
                                 f"Type must be one of 'n', 's', 'ns', or 't'. Skipping this entity.")
                else:
                    # If no type is provided, use the default from condition_included
                    if condition_included:
                        class_entities_list.append(entity)
                        types_list.append(condition_included)
                    else:
                        click.echo(f"Warning: No type specified for class entity '{entity}' and no default "
                                 f"condition provided. Skipping this entity.")
            
            if class_entities_list:
                puml_content = axiom_to_puml(
                    ontology=input,
                    class_entities=list(zip(class_entities_list, types_list)),
                    layout_type=layout,
                )
            else:
                click.echo("No valid class entities provided. Exiting.")
        elif class_included:
            # Legacy support for class_included option
            if condition_included:
                puml_content = axiom_to_puml(
                    ontology=input,
                    class_entities=class_included,
                    types=condition_included,
                    layout_type=layout,
                )
            else:
                click.echo("When using --class-included, you must also specify --condition-included. Exiting.")
        else:
            click.echo("No class entities provided. Use --class-entity or --class-included options. Exiting.")
    else:
        rdf_to_puml(
            input_rdf=input,
            relation_excluded=relation_excluded,
            layout_type=layout,
        )
 
    if view and puml_content:
        if not puml_file_path or not os.path.exists(puml_file_path):
            # If we don't have a valid file path, look for recently created PUML files
            puml_files = [f for f in os.listdir('.') if f.endswith('.puml')]
            if puml_files:
                # Sort by modification time, newest first
                puml_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
                puml_file_path = puml_files[0]
                click.echo(f"Using most recently created PUML file: {puml_file_path}")
        
        if puml_file_path:
            result = visualize_puml(puml_file_path, plantuml_server)
            if not result:
                click.echo("Note: If you're having issues with the PlantUML server, you can:")
                click.echo("1. Run a local server: docker run -d -p 8080:8080 plantuml/plantuml-server:jetty")
                click.echo("2. Use the PlantUML web server: --plantuml-server http://www.plantuml.com/plantuml/img/")
        else:
            click.echo("No PUML file found to visualize.")
    elif view:
        click.echo("No PUML content generated to visualize.")
 

if __name__ == "__main__":
    main(prog_name="nowl")