from owlready2 import *
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from nowlgen.generator.main import axiom_to_puml

get_ontology("benchmark-core-modified.rdf").load()
get_ontology("benchmark-simple-modified.rdf").load()
onto_simple = get_ontology("benchmark-simple-modified.rdf").load()
onto_complex = get_ontology("benchmark-complex.rdf").load()

# onto_simple_classes = [i for i in onto_simple.classes()]
# onto_complex_classes = [i for i in onto_complex.classes()]
#onto_complex.classes()
with open("complex_batch.md", "w") as f:
    for cls in onto_complex.classes():
        if cls.equivalent_to:
            converter = axiom_to_puml(
                class_entities={
                cls.iri: "ns",
                },
                ontology="benchmark-simple-modified.rdf",
                # layout_type="bipartite",
                save_puml=0,
            )
            # print(f"## Class: `{cls.iri}`\n\n```plantuml\n{converter[0]}\n```\n---")
            puml_content = converter[0].replace('\\n', '\n')
            f.write(f"{cls.iri}\n\n```plantuml\n{puml_content}\n```\n---\n")
        else:
            converter = axiom_to_puml(
                class_entities={
                cls.iri: "n",
                },
                ontology="benchmark-simple-modified.rdf",
                # layout_type="bipartite",
                save_puml=0,
            )
            # print(f"## Class: `{cls.iri}`\n\n```plantuml\n{converter[0]}\n```\n---")
            puml_content = converter[0].replace('\\n', '\n')
            f.write(f"{cls.iri}\n\n```plantuml\n{puml_content}\n```\n---\n")