from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

TRANSFORM_DICT = [
    # Foreign Key
    {
        "fhir_path": "id",
        "columns": {
            "observation_id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "code.coding",
        "columns": {
            "code_coding_system": {"fhir_key": "system", "type": "str"},
            "code_coding_code": {"fhir_key": "code", "type": "str"},
            "code_coding_display": {"fhir_key": "display", "type": "str"},
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
