from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_DICT = [
    # Foreign Key
    {
        "fhir_path": "id",
        "columns": {
            "observation_id": "id",
        },
    },
    {
        "fhir_path": "code.coding",
        "columns": {
            "category_coding_system": "system",
            "category_coding_code": "code",
            "category_coding_display": "display",
        },
    },
]


class ObservationCodeCodingTransformer(FhirResourceTransformer):
    """
    A transformer class for the 'Observation' resource in FHIR.

    Transform Patient JSON objects into flat dictionaries representing
    rows in an output CSV file

    Attributes:
        resource_type (str): The type of FHIR resource being transformed
        transform_dict (dict): The transformation dictionary used to map
          and transform the resource data

    Methods:
        __init__(self):
            Initializes the ObservationTransformer instance with the resource
            type 'Observation' and a transformation dictionary.
    """

    def __init__(self):
        super().__init__("Observation", "code_coding", TRANSFORM_DICT)
