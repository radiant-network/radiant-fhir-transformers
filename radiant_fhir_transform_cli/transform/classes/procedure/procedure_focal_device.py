"""
FHIR Procedure FocalDevice transformer
"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_SCHEMA = [
    # Primary Key
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
            "procedure_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "focalDevice",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "focal_device_action_coding": {
                "fhir_key": "action.coding",
                "type": "str",
            },
            "focal_device_action_text": {
                "fhir_key": "action.text",
                "type": "str",
            },
            "focal_device_manipulated_reference": {
                "fhir_key": "manipulated.reference",
                "type": "str",
            },
            "focal_device_manipulated_type": {
                "fhir_key": "manipulated.type",
                "type": "str",
            },
            "focal_device_manipulated_display": {
                "fhir_key": "manipulated.display",
                "type": "str",
            },
        },
    },
]


class ProcedureFocalDeviceTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'focalDevice' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'focalDevice' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('focal_device').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureFocalDeviceTransformer instance with the resource type 'Procedure',
            subtype 'focal_device', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", "focal_device", TRANSFORM_SCHEMA)
