import click

from rdf2puml import RdfToPumlConverter


def rdf_to_puml(input_rdf, output_puml):
    converter = RdfToPumlConverter(
        iofcore="https://spec.industrialontologies.org/ontology/core/Core/",
        bfo="http://purl.obolibrary.org/obo/")
    converter.convert(input_rdf, output_puml)


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument("input_rdf", type=click.Path(exists=True), metavar="<INPUT_RDF>")
@click.argument("output_puml", type=click.Path(), metavar="<OUTPUT_PUML>")
def main(input_rdf, output_puml):
    rdf_to_puml(input_rdf, output_puml)


if __name__ == "__main__":
    main(prog_name="rdf2puml")
