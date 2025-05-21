"""
FHIR Procedure PartOf transformer
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
        "fhir_path": "partOf",
        "fhir_reference": "part_of_reference",
        "columns": {
            "part_of_reference": {"fhir_key": "reference", "type": "str"},
            "part_of_type": {"fhir_key": "type", "type": "str"},
            "part_of_display": {"fhir_key": "display", "type": "str"},
        },
    },
]


class ProcedurePartOfTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'partOf' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'partOf' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('part_of').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureBasedOnTransformer instance with the resource type 'Procedure',
            subtype 'part_of', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", "part_of", TRANSFORM_SCHEMA)
