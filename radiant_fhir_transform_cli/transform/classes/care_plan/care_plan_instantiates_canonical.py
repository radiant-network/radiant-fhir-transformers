"""
FHIR CarePlan InstantiatesCanonical transformer
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
            "care_plan_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "instantiatesCanonical",
        "columns": {
            "instantiates_canonical": {"type": "str"},
        },
    },
]


class CarePlanInstantiatesCanonicalTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'CarePlan' resource in FHIR, focusing on the 'instantiatesCanonical' element.

    This class transforms FHIR CarePlan JSON objects into flat dictionaries suitable for CSV output,
    extracting and processing information from the 'instantiatesCanonical' field.

    Attributes:
        resource_type (str): The type of FHIR resource being transformed ('CarePlan').
        subtype (str): Specifies the sub-element of the resource to focus on ('instantiates_canonical').
        transform_dict (dict): A dictionary defining the mapping and transformation rules for the resource data.

    Methods:
        __init__():
            Initializes the CarePlanInstantiatesCanonicalTransformer instance with the resource type 'CarePlan',
            subtype 'instantiates_canonical', and the specified transformation dictionary.
    """

    def __init__(self):
        super().__init__("CarePlan", "instantiates_canonical", TRANSFORM_SCHEMA)
