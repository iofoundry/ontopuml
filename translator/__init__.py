import click

from translator.main import rdf_to_puml, axiom_to_puml


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument("input_rdf", type=click.Path(exists=True), metavar="<INPUT_RDF>")
@click.argument("output_puml", type=click.Path(), metavar="<OUTPUT_PUML>")
def main(input_rdf, output_puml):
    rdf_to_puml(input_rdf, output_puml)


if __name__ == "__main__":
    main(prog_name="rdf2puml")
