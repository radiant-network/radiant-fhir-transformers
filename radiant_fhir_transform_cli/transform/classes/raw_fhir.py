from typing import Any, override

from collections import defaultdict

from .base import FhirResourceTransformer

VIEW_DEFINITION = {
    "resourceType": "ViewDefinition",
    "resource": None,
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "id",
                },
                {
                    "name": "resource_type",
                    "path": "resourceType",
                },
                {
                    "name": "json",
                    "path": "$this",
                },
            ],
        },
    ],
}


class RawFhirResourceTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("fhir_resource", None, VIEW_DEFINITION)

    @override
    def transform_resources(
        self, resources: list[dict]
    ) -> list[dict[str, Any]]:
        resources_by_type = defaultdict(list)
        for resource in resources:
            resources_by_type[resource["resourceType"]].append(resource)

        output = []
        for resource_type, resource_list in resources_by_type.items():
            self.view_definition["resource"] = resource_type
            output.extend(super().transform_resources(resource_list))

        return output
