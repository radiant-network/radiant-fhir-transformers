"""
FHIR CarePlan PartOf transformer
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
        "fhir_path": "partOf",
        "fhir_reference": "part_of_reference",
        "columns": {
            "part_of_reference": {
                "fhir_key": "reference",
                "type": "str",
            },
            "part_of_display": {
                "fhir_key": "display",
                "type": "str",
            },
            "part_of_type": {
                "fhir_key": "type",
                "type": "str",
            },
        },
    },
]


class CarePlanPartOfTransformer(FhirResourceTransformer):
    """
    Transformer class for the 'CarePlan' resource in FHIR, focusing on the 'partOf' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'partOf' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('part_of').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanPartOfTransformer instance with the resource type 'CarePlan',
            subtype 'part_of', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "part_of", TRANSFORM_SCHEMA)
