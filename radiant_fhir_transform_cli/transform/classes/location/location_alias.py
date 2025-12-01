"""FHIR Location alias transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Location",
    "name": "location_alias",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "location_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "alias",
            "column": [{"name": "alias", "path": "$this", "type": "string"}],
        },
    ],
}


class LocationAliasTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Location", "alias", VIEW_DEFINITION)
