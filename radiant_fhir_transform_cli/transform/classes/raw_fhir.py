from .base import FhirResourceTransformer

TRANSFORM_SCHEMA = [
    # Id
    {
        "fhir_path": "id",
        "columns": {
            "id": {"fhir_key": "id", "type": "str"},
        },
    },
    {
        "fhir_path": "resourceType",
        "columns": {
            "resource_type": {"fhir_key": "resourceType", "type": "str"},
        },
    },
    {
        "fhir_path": "*",
        "columns": {
            "json": {"type": "str"},
        },
    },
]


class RawFhirResourceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("fhir_resource", None, TRANSFORM_SCHEMA)
