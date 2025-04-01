from owlready2 import get_ontology
from translator import axiom_to_puml

# Example usage
if __name__ == "__main__":
    # Example 1: Single class entity with single type
    converter1 = axiom_to_puml(
        "ProcuringBusinessProcess",
        "https://spec.industrialontologies.org/ontology/core/Core",
        types="ns",
        save_puml=False,
    )
    print("c1",converter1)

    # # Example 2: Multiple class entities with a single type (applied to all)
    # converter2 = axiom_to_puml(
    #     [
    #         "BusinessOrganization",
    #         "Manufacturer",
    #         "ProductProductionProcess",
    #         "MaterialProduct",
    #     ],
    #     "https://spec.industrialontologies.org/ontology/core/Core",
    #     types="ns",
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c2", converter2)

    # # Example 3: Same class entities with corresponding types
    # converter3 = axiom_to_puml(
    #     [
    #         "ComputingProcess",
    #         "ComputingProcess",
    #     ],
    #     "https://spec.industrialontologies.org/ontology/core/Core",
    #     types=["ns", "n"],
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c3",converter3)

    # Example 4: Multiple class entities with corresponding types (dictionary input)
    # converter4 = axiom_to_puml(
    #     class_entities={
    #         "BusinessOrganization": "ns",
    #         "http://purl.obolibrary.org/obo/BFO_0000040": "n",
    #         "ProductProductionProcess": "ns",
    #         "ManufacturerRole": "n",
    #         "BusinessFunction": "n",
    #         "SellingBusinessProcess": "n",
    #         "MaterialProduct": "ns",
    #     },
    #     ontology="https://spec.industrialontologies.org/ontology/core/Core",
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c4",converter4)

    # Example 5: Multiple class entities with corresponding types (IRI dictionary input)
    converter5 = axiom_to_puml(
        class_entities={
        "https://spec.industrialontologies.org/ontology/core/Core/GainOfRole": "ns",
        # "https://spec.industrialontologies.org/ontology/core/Core/Organization": "n",
        # "ProductProductionProcess": "ns",
        # "http://purl.obolibrary.org/obo/BFO_0000023": "n",
        # "https://spec.industrialontologies.org/ontology/core/Core/Agent": "n",
        # "MaterialProduct": "ns",
        },
        ontology="https://spec.industrialontologies.org/ontology/core/Core",
        layout_type="bipartite",
        save_puml=0,
    )
    print("c5",converter5)


   # Example 6: Multiple class entities with corresponding types (tuple input)
    # converter6 = axiom_to_puml(
    #     class_entities=[
    #         ("ComputingProcess", "ns"),
    #         ("https://spec.industrialontologies.org/ontology/core/Core/Organization", "n"),
    #         ("ProductProductionProcess", "ns"),
    #         ("http://purl.obolibrary.org/obo/BFO_0000023", "n"),
    #         ("https://spec.industrialontologies.org/ontology/core/Core/Agent", "n"),
    #         ("MaterialProduct", "ns"),
    #     ],
    #     ontology="https://spec.industrialontologies.org/ontology/core/Core",
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c6",converter6)

"""
Methods

Constructor (`__init__`)
**Purpose**: Initializes the `PumlAxiomGenerator` object with necessary parameters and sets up the graph 
structure.

- **Parameters**:
  - `class_entities`: A list of class entities to process.
  - `types`: A list specifying the type of axiom for each class entity (e.g., "ns" for equivalent_to, "s" for 
general_class_axiom).
  - `graph` (optional): An existing NetworkX graph; defaults to a new empty graph.
  - `node_labels` (optional): Dictionary mapping nodes to their labels; defaults to an empty dictionary.
  - `layout_type` (optional): Layout algorithm for the graph (e.g., "forceatlas2", "fr" for Fruchterman-Reingold, 
etc.).
  - `visualize` (optional): Boolean indicating if visualization should be generated; defaults to True.
  - `save_puml` (optional): Boolean indicating if the PUML output should be saved to a file; defaults to False.

---

`convert()`
**Purpose**: Converts class entities and their axioms into PUML syntax, applying optimized directions where 
necessary.

- **Steps**:
  1. Processes each class entity based on its axiom type (equivalent_to, general_class_axiom, subclass).
  2. Finalizes the PUML output by appending the `@enduml` command if not already present.
  3. Applies NetworkX layout to determine node positions and edge directions.
  4. Visualizes the graph using `_visualize_graph()` if enabled.
  5. Saves the PUML output to a file if specified.
  6. Returns the formatted PUML output as a string.

---

`_apply_directions_to_puml()`
**Purpose**: Modifies the PUML output by adding directions to specific relationships based on edge directions 
calculated in the graph.

- **Parameters**:
  - `edge_directions`: Dictionary mapping tuples of (source, target) to their respective directions.

- **Returns**:
  - The updated list of PUML lines with directions applied.

---

`_calculate_layout()`
**Purpose**: Calculates the layout of the graph using a specified algorithm or defaults to "forceatlas2" if 
unspecified.

- **Returns**:
  - A NetworkX graph object with nodes positioned according to the chosen layout.

---

`_calculate_directions()`
**Purpose**: Determines edge directions for the graph based on the current node positions, enhancing visual 
clarity.

- **Returns**:
  - Edge directions stored in a dictionary for use in `_apply_directions_to_puml()`.

---

#### `_visualize_graph()`
**Purpose**: Visualizes the graph using matplotlib, incorporating node labels and edge directions if available.

- **Parameters**:
  - `show` (optional): Boolean indicating if the plot should be displayed; defaults to True.
  - `savefig` (optional): Filename for saving the visualization; defaults to None.

---

### Notes
1. The code supports multiple axiom types, but some functionality (e.g., general_class_axiom) is currently 
commented out and may require further implementation.
2. If no layout type is specified, "forceatlas2" is used as the default algorithm for positioning nodes in the 
graph.

---
"""