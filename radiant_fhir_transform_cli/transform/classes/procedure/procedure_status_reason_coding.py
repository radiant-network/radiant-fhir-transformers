"""
FHIR Procedure StatusReason Coding transformer
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
        "fhir_path": "statusReason.coding",
        "columns": {
            "status_reason_coding_system": {
                "fhir_key": "system",
                "type": "str",
            },
            "status_reason_coding_code": {"fhir_key": "code", "type": "str"},
            "status_reason_coding_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ProcedureStatusReasonCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'statusReason.coding' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'statusReason.coding' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('status_reason_coding').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureStatusReasonCodingTransformer instance with the resource type 'Procedure',
            subtype 'status_reason_coding', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", "status_reason_coding", TRANSFORM_SCHEMA)
