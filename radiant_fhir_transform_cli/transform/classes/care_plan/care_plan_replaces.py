"""
FHIR CarePlan Replacestransformer
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
            "care_plan_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "replaces",
        "fhir_reference": "replaces_reference",
        "columns": {
            "replaces_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "replaces_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "replaces_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class CarePlanReplacesTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'CarePlan' resource in FHIR, focusing on the 'replaces' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'replaces' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('replaces').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanReplacesTransformer instance with the resource type 'CarePlan',
            subtype 'replaces', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "replaces", TRANSFORM_SCHEMA)
