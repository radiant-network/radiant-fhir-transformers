"""
FHIR CarePlan Based On transformer
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
        "fhir_path": "basedOn",
        "fhir_reference": "based_on_reference",
        "columns": {
            "based_on_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "based_on_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "based_on_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class CarePlanBasedOnTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'CarePlan' resource in FHIR, focusing on the 'basedOn' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'basedOn' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('based_on').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanBasedOnTransformer instance with the resource type 'CarePlan',
            subtype 'based_on', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "based_on", TRANSFORM_SCHEMA)
