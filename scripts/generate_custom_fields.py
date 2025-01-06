# SPDX-FileCopyrightText: Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
# %%

import pathlib
import typing as t

from lxml import builder, etree

CUSTOM_FIELDS_PATH = pathlib.Path(__file__).parents[1] / "global" / "fields"
TYPE_ENUM_PATH = CUSTOM_FIELDS_PATH / "workitem-type-enum.xml"

FIELDS: dict[str, t.Any] = {
    "Generic Capella Fields": {
        "uuid_capella": {
            "name": "UUID (Capella)",
            "description": "Corresponding Capella ID",
            "type": "string",
        },
        "checksum": {
            "name": "Checksum",
            "description": "A checksum-hash of the work item for efficient comparison "
            "for the SET Toolchain.",
            "type": "string",
        },
        "parent": {
            "name": "Parent",
            "description": "Grouped links for parent.",
            "type": "text/html",
        },
        "parent_reverse": {
            "name": "Children",
            "description": "Grouped links backlinks for parent.",
            "type": "text/html",
        },
        "layer": {
            "name": "Layer",
            "description": "The layer of the work item.",
            "type": "enum:_C2P_layer",
        },
    },
    "Requirement Fields": {
        "assumption": {
            "name": "Assumption",
            "description": "Requirement text from a Requirement of type Assumption.",
            "type": "text/html",
        },
        "availability": {
            "name": "Availability",
            "description": "Requirement text from a Requirement of type Availability.",
            "type": "text/html",
        },
        "computation": {
            "name": "Computation",
            "description": "Requirement text from a Requirement of type Computation.",
            "type": "text/html",
        },
        "legal": {
            "name": "Legal",
            "description": "Requirement text from a Requirement of type Legal.",
            "type": "text/html",
        },
        "performance": {
            "name": "Performance",
            "description": "Requirement text from a Requirement of type Performance.",
            "type": "text/html",
        },
        "rationale": {
            "name": "Rationale",
            "description": "Requirement text from a Requirement of type Rationale.",
            "type": "text/html",
        },
        "reliability": {
            "name": "Reliability",
            "description": "Requirement text from a Requirement of type Reliability.",
            "type": "text/html",
        },
        "safety": {
            "name": "Safety",
            "description": "Requirement text from a Requirement of type Safety.",
            "type": "text/html",
        },
        "security": {
            "name": "Security",
            "description": "Requirement text from a Requirement of type Security.",
            "type": "text/html",
        },
        "standards": {
            "name": "Standards",
            "description": "Requirement text from a Requirement of type Standards.",
            "type": "text/html",
        },
    },
    "Custom Capella Fields": {
        "preCondition": {
            "name": "Pre Condition",
            "description": "Pre Condition.",
            "type": "text/html",
        },
        "postCondition": {
            "name": "Post Condition",
            "description": "Post Condition.",
            "type": "text/html",
        },
        "nature": {
            "name": "Nature",
            "description": "The nature of a PhysicalComponent.",
            "type": "string",
        },
        "kind": {
            "name": "Kind",
            "description": "The kinds for various types.",
            "type": "string",
        },
        "allocated_functions": {
            "name": "Allocated functions",
            "description": "Grouped links for allocated funtions.",
            "type": "text/html",
        },
        "allocated_functions_reverse": {
            "name": "Allocated as a function by",
            "description": "Grouped links backlinks for allocated functions.",
            "type": "text/html",
        },
        "allocated_functional_exchanges": {
            "name": "Allocated functional exchanges",
            "description": "Grouped links for allocated functional exchanges.",
            "type": "text/html",
        },
        "allocated_functional_exchanges_reverse": {
            "name": "Allocated as a functional Exchange by",
            "description": "Grouped links backlinks for allocated functional exchanges.",
            "type": "text/html",
        },
        "exchange_items": {
            "name": "Exchange items",
            "description": "Grouped links for exchange items.",
            "type": "text/html",
        },
        "exchange_items_reverse": {
            "name": "Exchange item in",
            "description": "Grouped links backlinks for exchange items.",
            "type": "text/html",
        },
        "involved_activities": {
            "name": "Involved activities",
            "description": "Grouped links for involved activities.",
            "type": "text/html",
        },
        "involved_activities_reverse": {
            "name": "Involved as an activity by",
            "description": "Grouped links backlinks for involved activities.",
            "type": "text/html",
        },
        "involved_entities": {
            "name": "Involved entities",
            "description": "Grouped links for involved entities.",
            "type": "text/html",
        },
        "involved_entities_reverse": {
            "name": "Involved by",
            "description": "Grouped links backlinks for involved entities.",
            "type": "text/html",
        },
        "diagram_elements": {
            "name": "Diagram elements",
            "description": "Grouped links for diagram elements.",
            "type": "text/html",
        },
        "diagram_elements_reverse": {
            "name": "Diagrams",
            "description": "Grouped links backlinks for diagram elements.",
            "type": "text/html",
        },
        "state_machines": {
            "name": "State machines",
            "description": "Grouped links for state machines.",
            "type": "text/html",
        },
        "state_machines_reverse": {
            "name": "State machine in",
            "description": "Grouped links backlinks for state machines.",
            "type": "text/html",
        },
        "constraints": {
            "name": "Constraints",
            "description": "Grouped links for constraints.",
            "type": "text/html",
        },
        "constraints_reverse": {
            "name": "Constraints",
            "description": "Grouped links backlinks for constraints.",
            "type": "text/html",
        },
        "output_exchanges": {
            "name": "Output exchanges",
            "description": "Grouped links for output functional exchanges.",
            "type": "text/html",
        },
        "output_exchanges_reverse": {
            "name": "Output exchange in",
            "description": "Grouped links backlinks for output functional exchanges.",
            "type": "text/html",
        },
        "input_exchanges": {
            "name": "Input exchanges",
            "description": "Grouped links for input functional exchanges.",
            "type": "text/html",
        },
        "input_exchanges_reverse": {
            "name": "Input exchange in",
            "description": "Grouped links backlinks for input functional exchanges.",
            "type": "text/html",
        },
        "activities": {
            "name": "Activities",
            "description": "Grouped links for activities.",
            "type": "text/html",
        },
        "activities_reverse": {
            "name": "Activity in",
            "description": "Grouped links backlinks for activities.",
            "type": "text/html",
        },
        "outputs": {
            "name": "Outputs",
            "description": "Grouped links for outputs.",
            "type": "text/html",
        },
        "outputs_reverse": {
            "name": "Output in",
            "description": "Grouped links backlinks for outputs.",
            "type": "text/html",
        },
        "inputs": {
            "name": "Inputs",
            "description": "Grouped links for inputs.",
            "type": "text/html",
        },
        "inputs_reverse": {
            "name": "Input in",
            "description": "Grouped links backlinks for inputs.",
            "type": "text/html",
        },
        "description_reference": {
            "name": "Description references",
            "description": "Grouped links for description references.",
            "type": "text/html",
        },
        "description_reference_reverse": {
            "name": "Referenced in description by",
            "description": "Grouped links backlinks for descriptions references.",
            "type": "text/html",
        },
        "scenarios": {
            "name": "Scenarios",
            "description": "Grouped links for scenarios.",
            "type": "text/html",
        },
        "scenarios_reverse": {
            "name": "is Scenario in",
            "description": "Grouped links backlinks for scenarios.",
            "type": "text/html",
        },
        "involved_functions": {
            "name": "Involved Functions",
            "description": "Involved functions on a FunctionalChain",
            "type": "text/html",
        },
        "involved_functions_reverse": {
            "name": "Involved function in",
            "description": "Grouped links backlinks for involved_functions.",
            "type": "text/html",
        },
        "involved_links": {
            "name": "Involved Links",
            "description": "Involved exchanges on a FunctionalChain.",
            "type": "text/html",
        },
        "involved_links_reverse": {
            "name": "Involved exchange in",
            "description": "Grouped links backlinks for involve",
            "type": "text/html",
        },
        "realized_functions": {
            "name": "Realized functions",
            "description": "Realized functions of a SystemFunction.",
            "type": "text/html",
        },
        "realized_functions_reverse": {
            "name": "Realizing functions",
            "description": "Grouped links backlinks for realized functions.",
            "type": "text/html",
        },
        "involved_components": {
            "name": "Involved Components",
            "description": "Involved components on a Capability.",
            "type": "text/html",
        },
        "involved_components_reverse": {
            "name": "Involved exchange in",
            "description": "Grouped links backlinks for involved_components.",
            "type": "text/html",
        },
        "involved_chains": {
            "name": "Involved Chains",
            "description": "Involved chains on a Capability or FunctionalChain.",
            "type": "text/html",
        },
        "involved_chains_reverse": {
            "name": "Involved chain in",
            "description": "Grouped links backlinks for involved_chains.",
            "type": "text/html",
        },
        "realized_components": {
            "name": "Realized Components",
            "description": "Realized components of a Component.",
            "type": "text/html",
        },
        "realized_components_reverse": {
            "name": "Realizing components",
            "description": "Grouped links backlinks for realized_components.",
            "type": "text/html",
        },
        "realized_capabilities": {
            "name": "Realized Capabilities",
            "description": "Realized capabilities of a Capability.",
            "type": "text/html",
        },
        "realized_capabilities_reverse": {
            "name": "Realizing capability",
            "description": "Grouped links backlinks for realized_capabilities.",
            "type": "text/html",
        },
        "related_functions": {
            "name": "Related Functions",
            "description": "Related functions of a Scenario.",
            "type": "text/html",
        },
        "related_functions_reverse": {
            "name": "Related function in",
            "description": "Grouped links backlinks for related_functions.",
            "type": "text/html",
        },
        "includes": {
            "name": "Includes",
            "description": "Included Capabilities.",
            "type": "text/html",
        },
        "includes_reverse": {
            "name": "Included in",
            "description": "Grouped links backlinks for includes.",
            "type": "text/html",
        },
        "extends": {
            "name": "Extends",
            "description": "Extended Capabilities.",
            "type": "text/html",
        },
        "extends_reverse": {
            "name": "Extended in",
            "description": "Grouped links backlinks for extends.",
            "type": "text/html",
        },
        "generalizes": {
            "name": "Generalizes",
            "description": "Generalized Capabilities.",
            "type": "text/html",
        },
        "generalizes_reverse": {
            "name": "Generalized in",
            "description": "Grouped links backlinks for generalizes.",
            "type": "text/html",
        },
        "interfaces": {
            "name": "Interfaces",
            "description": "Interfaces between Components and Actors.",
            "type": "text/html",
        },
        "interfaces_reverse": {
            "name": "Interface in",
            "description": "Grouped links backlinks for interfaces.",
            "type": "text/html",
        },
        "physical_links": {
            "name": "Physical Links",
            "description": "Physical links for connecting Physical Component Nodes.",
            "type": "text/html",
        },
        "physical_links_reverse": {
            "name": "Physical link in",
            "description": "Grouped links backlinks for physical links.",
            "type": "text/html",
        },
    },
    "Custom Diagram Fields": {
        "context_diagram": {
            "name": "Context Diagram",
            "description": "Context Diagram",
            "type": "text/html",
        },
        "tree_view": {
            "name": "Tree View Diagram",
            "description": "Tree View Diagram",
            "type": "text/html",
        },
        "realization_view": {
            "name": "Realization View Diagram",
            "description": "Realization View Diagram",
            "type": "text/html",
        },
        "cable_tree": {
            "name": "Cable Tree Diagram",
            "description": "Cable Tree Diagram",
            "type": "text/html",
        },
    },
}


def generate_custom_field_xml_files(xml_file: pathlib.Path):
    """Generate custom-fields.xml for every workitem type."""
    tree = etree.parse(xml_file)
    root = tree.getroot()
    all_fields = (
        FIELDS["Generic Capella Fields"]
        | FIELDS["Requirement Fields"]
        | FIELDS["Custom Capella Fields"]
        | FIELDS["Custom Diagram Fields"]
    )

    E = builder.ElementMaker()
    for option in root.findall(".//option"):
        if type_id := option.get("id"):
            filename = f"{type_id}-custom-fields.xml"
            field_items = [
                E.field(
                    id=id,
                    name=field["name"],
                    type=field["type"],
                    description=field["description"],
                )
                for id, field in all_fields.items()
            ]
            fields_element = E.fields(*field_items)

            declaration = "<?xml version='1.0' encoding='UTF-8'?>\n"
            comment = (
                "<!-- SPDX-FileCopyrightText: Copyright DB InfraGO AG "
                "and contributors\nSPDX-License-Identifier: Apache-2.0 -->\n"
            )
            fields = etree.tostring(fields_element, pretty_print=True, encoding=str)
            content = declaration + comment + fields

            (xml_file.parent / filename).write_text(content, encoding="utf8")
            print(f"Generated file: {filename!r}")


def generate_form_layout_xml_files(xml_file: pathlib.Path):
    """Generate form-layout.xml for every workitem type."""
    tree = etree.parse(xml_file)
    root = tree.getroot()

    NSMAP = {
        None: "http://polarion.com/schema/WorkItems/FormLayout",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    }
    E = builder.ElementMaker(namespace=NSMAP[None], nsmap=NSMAP)
    fields = (
        FIELDS["Generic Capella Fields"]
        | FIELDS["Requirement Fields"]
        | FIELDS["Custom Diagram Fields"]
    )
    custom_fields_id_attributes = ",".join(f"-{fid}" for fid in fields)
    for option in root.findall(".//option"):
        if type_id := option.get("id"):
            generic_fields = [
                E.field(id=field_id, readOnly="true")
                for field_id in FIELDS["Generic Capella Fields"]
            ]
            custom_fields_id = (
                "@allCustomFields,-owner,-sortOrder,-manualQuality,"
                "-qualitySuspect,-automatics,-language," + custom_fields_id_attributes
            )
            custom_diagram_fields = [
                E.field(id=field_id, readOnly="true")
                for field_id in FIELDS["Custom Diagram Fields"]
            ]
            requirement_fields = [
                E.field(id=field_id, readOnly="true")
                for field_id in FIELDS["Requirement Fields"]
            ]

            form_layout = E.formLayout(
                E.horizontal(
                    E.vertical(E.section(E.field(id="type"), E.field(id="project")))
                ),
                E.field(id="description"),
                E.panel(*generic_fields, description="Generic Capella Fields"),
                E.panel(
                    E.field(id=custom_fields_id, readOnly="true"),
                    *custom_diagram_fields,
                    description="Custom Capella Fields",
                ),
                E.panel(*requirement_fields, description="Requirement Fields"),
                E.field(id="comments"),
                E.field(id="linkedWorkItems"),
                E.field(id="hyperlinks"),
            )
            form_layout.set(
                f"{{{NSMAP['xsi']}}}schemaLocation",
                "http://polarion.com/schema/WorkItems/FormLayout",
            )

            declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
            comment = (
                "<!-- SPDX-FileCopyrightText: Copyright DB InfraGO AG "
                "and contributors\nSPDX-License-Identifier: Apache-2.0 -->\n"
            )
            layout = etree.tostring(form_layout, pretty_print=True, encoding=str)
            content = declaration + comment + layout

            filename = f"{type_id}-form-layout.xml"
            root_path = xml_file.parent.parent / "hats" / "_default" / "tracker"
            (root_path / filename).write_text(content, encoding="utf8")
            print(f"Generated file: {filename!r}")


# %%
if __name__ == "__main__":
    generate_custom_field_xml_files(TYPE_ENUM_PATH)
    generate_form_layout_xml_files(TYPE_ENUM_PATH)

# %%
