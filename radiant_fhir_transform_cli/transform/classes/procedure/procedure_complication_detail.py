"""
FHIR Procedure ComplicationDetail transformer
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
        "fhir_path": "complicationDetail",
        "fhir_reference": "complication_detail_reference",
        "columns": {
            "complication_detail_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "complication_detail_display": {
                "fhir_key": "display",
                "type": "str",
            },
        },
    },
]


class ProcedureComplicationDetailTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Procedure' resource in FHIR, focusing on the 'complicationDetail' element.

    This class transforms FHIR Procedure JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'complicationDetail' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('Procedure').
        subtype (str): Specifies the sub-element of the resource to focus on ('complication_detail').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the ProcedureComplicationDetailTransformer instance with the resource type 'Procedure',
            subtype 'complication_detail', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("Procedure", "complication_detail", TRANSFORM_SCHEMA)
