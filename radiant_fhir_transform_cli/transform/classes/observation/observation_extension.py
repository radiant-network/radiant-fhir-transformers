"""
FHIR Observation Extension transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    {
        "fhir_path": None,
        "columns": {
            "id": {"fhir_key": None, "type": "str"},
        },
    },
    # Foreign Key
    {
        "fhir_path": "id",
        "is_foreign_key": True,
        "columns": {
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "extension",
        "columns": {
            "extension_url": {
                "fhir_key": "url",
                "type": "str",
            },
            "extension_value_identifier_system": {
                "fhir_key": "valueIdentifier.system",
                "type": "str",
            },
            "extension_value_identifier_value": {
                "fhir_key": "valueIdentifier.value",
                "type": "str",
            },
        },
    },
]


class ObservationExtensionTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'Observation' resource in FHIR, focusing on the 'extension' element.

    This class transforms FHIR Observation JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'extension' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Observation').
        subtype (str): Specifies the sub-element of the resource to focus on ('extension').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ObservationCategoryCodingTransformer instance with the resource type 'Observation',
            subtype 'category.coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "extension", TRANSFORM_SCHEMA)
