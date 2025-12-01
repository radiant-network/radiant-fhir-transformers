from typing import Any, override

from .base import FhirResourceTransformer

VIEW_DEFINITION = {
    "resourceType": "ViewDefinition",
    "resource": None,
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

    @override
    def transform_resource(
        self, resource_idx: int, resource_dict: dict[str, Any]
    ) -> list[dict[str, Any]]:
        resource_type = resource_dict["resourceType"]
        self.view_definition["resource"] = resource_type
        return super().transform_resource(resource_idx, resource_dict)
