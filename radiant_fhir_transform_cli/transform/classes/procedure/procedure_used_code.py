"""
FHIR Procedure UsedCode transformer
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
        "fhir_path": "usedCode",
        "columns": {
            # TODO: Support for Nested Lists (See https://github.com/radiant-network/radiant-fhir-transformers/issues/34)
            "used_code_coding": {"fhir_key": "coding", "type": "str"},
            "used_code_text": {"fhir_key": "text", "type": "str"},
        },
    },
]


class ProcedureUsedCodeTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'usedCode' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'usedCode' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('used_code').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureUsedCodeTransformer instance with the resource type 'Procedure',
            subtype 'used_code', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", "used_code", TRANSFORM_SCHEMA)
