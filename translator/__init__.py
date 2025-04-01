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
    type=click.Path(exists=True),
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
    "--class-included",
    default=[],
    type=IRI,
    help="(optional) List of classes to include in the object diagram.\n"
    "If -c is set, only axioms from these classes are included in the class diagram.\n"
    "Expect full IRIs.",
)
@click.option(
    "--relation-excluded",
    multiple=True,
    type=IRI,
    help="(optional) List of relations to exclude between instances in the object diagram. Has no effect on class diagrams.",
)
@click.option(
    "--condition-included",
    type=click.Choice(["n", "s", "ns"]),
    help="(optional) Determines which axioms to include in the class diagram.\n"
    "'n' - Necessary conditions (subclass axioms).\n"
    "'s' - Sufficient conditions (general class axioms).\n"
    "'ns' - Necessary & sufficient conditions (equivalent class axioms).",
)
@click.option(
    "-l",
    "--layout",
    default="spring",
    show_default=True,
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
@click.option("--help", is_flag=True, help="Show this help message and exit.")
def main(
    input,
    class_diagram,
    class_included,
    relation_excluded,
    condition_included,
    layout,
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

    if class_diagram:
        axiom_to_puml(
            ontology=input, class_entities = class_included, types=condition_included, layout_type=layout
        ) 
    else:
        rdf_to_puml(ontology=input, relation_excluded=relation_excluded, layout_type=layout)
 

if __name__ == "__main__":
    main(prog_name="ontoplant")
