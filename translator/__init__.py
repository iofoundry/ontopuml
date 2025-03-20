import os

import click

from translator.main import rdf_to_puml, axiom_to_puml


class IRIParamType(click.ParamType):
    name = "IRI"

    def convert(self, value, param, ctx):
        return value


IRI = IRIParamType()


def find_ontology_file():
    """Search for an ontology file in the current directory."""
    extensions = [".rdf", ".owl", ".ttl", ".jsonld"]
    for file in os.listdir():
        if any(file.endswith(ext) for ext in extensions):
            return file
    return None


@click.command(context_settings={
    "ignore_unknown_options": True,
    "help_option_names": ["--help"],
    "terminal_width": 100
})
@click.option("-i", "--input", type=click.Path(exists=True),
              help="(optional) Input ontology file. Supported formats: .rdf, .owl, .ttl, .jsonld.\n"
                   "If not provided, the tool will search for an ontology file in the current directory.")
@click.option("-o", "--output", type=click.Path(),
              help="(optional) Output PlantUML (.puml) file path.\n"
                   "If not provided, the output is saved in the same directory as the input file with a '.puml' extension.")
@click.option("-c", "--class-diagram", is_flag=True,
              help="(optional) Generates a class diagram.\n"
                   "By default, only an object diagram is generated.")
@click.option("--class-included", multiple=True, type=IRI,
              help="(optional) List of classes to include in the object diagram.\n"
                   "If -c is set, only axioms from these classes are included in the class diagram.\n"
                   "Expect full IRIs.")
@click.option("--relation-excluded", multiple=True, type=IRI,
              help="(optional) List of relations to exclude between instances in the object diagram. Has no effect on class diagrams.")
@click.option("--condition-included", type=click.Choice(["n", "s", "ns"]),
              help="(optional) Determines which axioms to include in the class diagram.\n"
                   "'n' - Necessary conditions (subclass axioms).\n"
                   "'s' - Sufficient conditions (general class axioms).\n"
                   "'ns' - Necessary & sufficient conditions (equivalent class axioms).")
@click.option("-l", "--layouts", multiple=True,
              help="(optional) Specifies the layout algorithm(s) to use.")
@click.option("-q", "--quick-layout", is_flag=True,
              help="(optional) Enables quick layout mode for class diagrams.")
@click.option("--help", is_flag=True,
              help="Show this help message and exit.")
def main(input, output, class_diagram,
         class_included, relation_excluded, condition_included,
         layouts, quick_layout, help):
    if help:
        click.echo(click.get_current_context().get_help())
        return

    if input is None:
        click.echo("No input file provided. Searching for an ontology file in the current directory...")
        input = find_ontology_file()
        if input is None:
            click.echo("No ontology file found. Exiting.")
            return
        click.echo(f"Using found ontology file: {input}")

    if output is None and input:
        output = f"{input}.puml"

    if class_diagram:
        axiom_to_puml(input, output, class_included, condition_included)
    else:
        rdf_to_puml(input, output, relation_excluded)


if __name__ == "__main__":
    main(prog_name="ontoplant")
