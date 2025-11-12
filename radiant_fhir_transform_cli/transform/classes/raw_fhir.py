from .base import FhirResourceTransformer

VIEW_DEFINITION = {
    "resourceType": "ViewDefinition",
    "resource": "Observation",
    "select": [
        {
            "column": [
                {"name": "id", "path": "id"},
                {"name": "resource_type", "path": "resourceType"},
                {"name": "json", "path": "$this"},
            ]
        },
    ],
}


class RawFhirResourceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("fhir_resource", None, VIEW_DEFINITION)
