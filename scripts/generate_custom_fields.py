# SPDX-FileCopyrightText: Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
# %%

import json
import pathlib
import typing as t

import yaml
from lxml import builder, etree

SCRIPTS_PATH = pathlib.Path(__file__).parents[0]
GLOBAL_CUSTOM_FIELDS_PATH = pathlib.Path(__file__).parents[1] / "global" / "fields"
GLOBAL_TYPE_ENUM_PATH = GLOBAL_CUSTOM_FIELDS_PATH / "workitem-type-enum.xml"
CUSTOM_FIELDS_PATH = (
    pathlib.Path(__file__).parents[1] / "template" / ".polarion" / "tracker" / "fields"
)
TYPE_ENUM_PATH = CUSTOM_FIELDS_PATH / "workitem-type-enum.xml"
CAPELLAMBSE_CUSTOM_FIELDS_PATH = SCRIPTS_PATH / "data" / "capellambse-fields.json"
LINK_FIELDS_PATH = SCRIPTS_PATH / "data" / "link-fields.json"
CAPELLA_ICON_URL_PATH = SCRIPTS_PATH / "data" / "capella-iconURL.json"

ICON_URL_TEMPLATE = "/polarion/icons/project/%project-id%/"

C2P_FIELDS: dict[str, t.Any] = {
    "ALL": {
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
    }
}
REQUIREMENT_FIELDS: dict[str, t.Any] = {
    "ALL": {
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
    }
}
"""XXX: Check against the model what RequirementTypes are available."""
CAPELLAMBSE_FIELDS = json.loads(
    CAPELLAMBSE_CUSTOM_FIELDS_PATH.read_text(encoding="utf8")
)
LINK_FIELDS = json.loads(LINK_FIELDS_PATH.read_text(encoding="utf8"))

CUSTOM_FIELDS: dict[str, t.Any] = CAPELLAMBSE_FIELDS | LINK_FIELDS
for fields in CUSTOM_FIELDS.values():
    fields.update(C2P_FIELDS["ALL"] | REQUIREMENT_FIELDS["ALL"])


def generate_polarion_config_files(
    config: pathlib.Path, dest: pathlib.Path, type_prefix: str = ""
):
    c2p_map = extract_polarion_types_from_config(config)
    c2icons = json.loads(CAPELLA_ICON_URL_PATH.read_text(encoding="utf8"))

    E = builder.ElementMaker()
    options = []
    for i, (model_element, p_types) in enumerate(c2p_map.items(), start=1):
        for p_type in p_types:
            if (custom_fields := CUSTOM_FIELDS.get(model_element)) is None:
                print(f"Unknown Capella type: {model_element!r}")
                continue

            oid = p_type
            if type_prefix and model_element != "Diagram":
                oid = f"{type_prefix}_{p_type}"

            iconURL = c2icons.get(model_element, ICON_URL_TEMPLATE)

            options.append(
                E.option(
                    id=oid,
                    name=p_type[0].upper() + p_type[1:],
                    description=f"Represents a {model_element} in Capella.",
                    iconURL=iconURL,
                    sortOrder=str(i),
                )
            )

            filename = f"{oid}-custom-fields.xml"
            field_items = [
                E.field(
                    id=id,
                    type=field["type"],
                    name=field["name"],
                    description=field["description"],
                )
                for id, field in custom_fields.items()
            ]
            generate_xml_file(E.fields(*field_items), dest=dest, filename=filename)

    generate_xml_file(
        E.enumeration(*options), dest=dest, filename="workitem-type-enum.xml"
    )


def extract_polarion_types_from_config(config: pathlib.Path) -> dict[str, set[str]]:
    data = yaml.safe_load(config.read_text(encoding="utf8"))

    def resolve_element_type(p_type: str) -> str:
        """Return a valid Type ID for polarion for a given ``obj``."""
        return p_type[0].lower() + p_type[1:]

    object_type_to_polarion_type: dict[str, set[str]] = {}
    for model_element in data.values():
        for element_type, element_config in model_element.items():
            if element_type == "*":
                continue

            if isinstance(element_config, dict):
                p_type = element_config.get(
                    "polarion_type", resolve_element_type(element_type)
                )
                object_type_to_polarion_type.setdefault(element_type, set()).add(p_type)
            elif isinstance(element_config, list):
                for econfig in element_config:
                    if (p_type := econfig.get("polarion_type")) is None:
                        continue

                    object_type_to_polarion_type.setdefault(element_type, set()).add(
                        p_type
                    )
            elif element_config is None:
                p_type = resolve_element_type(element_type)
                object_type_to_polarion_type.setdefault(element_type, set()).add(p_type)
    return object_type_to_polarion_type


def generate_custom_field_xml_files(xml_file: pathlib.Path, type_prefix: str = "_C2P"):
    """Generate custom-fields.xml for every workitem type."""
    tree = etree.parse(xml_file)
    root = tree.getroot()

    E = builder.ElementMaker()
    for option in root.findall(".//option"):
        if type_id := option.get("id"):
            _type_id = type_id.removeprefix(f"{type_prefix}_")
            _type_id = _type_id[0].upper() + _type_id[1:]
            if not (fields := CUSTOM_FIELDS.get(_type_id, {})):
                print(f"No custom fields found for {type_id!r}")
                continue

            filename = f"{type_id}-custom-fields.xml"
            field_items = [
                E.field(
                    id=id,
                    name=field["name"],
                    description=field["description"],
                    type=field["type"],
                )
                for id, field in fields.items()
            ]
            generate_xml_file(
                E.fields(*field_items), dest=xml_file.parent, filename=filename
            )


def generate_xml_file(
    parent_element: etree._Element, dest: pathlib.Path, filename: str
):
    """Create an XML file."""
    declaration = "<?xml version='1.0' encoding='UTF-8'?>\n"
    comment = (
        "<!-- SPDX-FileCopyrightText: Copyright DB InfraGO AG "
        "and contributors\nSPDX-License-Identifier: Apache-2.0 -->\n"
    )
    xml = etree.tostring(parent_element, pretty_print=True, encoding=str)
    content = declaration + comment + xml
    (dest / filename).write_text(content, encoding="utf8")
    print(f"Generated file: {filename!r}")


def _get_iconURL_map(xml_file: pathlib.Path, type_prefix: str = "") -> dict[str, str]:
    tree = etree.parse(xml_file)
    root = tree.getroot()
    model_element_to_icons = {}
    for option in root.findall(".//option"):
        pid = option.get("id").removeprefix(type_prefix)
        pid = pid[0].upper() + pid[1:]
        model_element_to_icons[pid] = option.get("iconURL", ICON_URL_TEMPLATE)
    return model_element_to_icons


# %%
if __name__ == "__main__":
    generate_custom_field_xml_files(GLOBAL_TYPE_ENUM_PATH)

    # config_path = pathlib.Path(...)
    # generate_polarion_config_files(config_path, dest=SCRIPTS_PATH / "config")


# %%
