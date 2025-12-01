"""FHIR Coverage contract transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Coverage",
    "name": "coverage_contract",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "coverage_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "contract",
            "column": [
                {
                    "name": "contract_reference",
                    "path": "reference",
                    "type": "string",
                },
                {"name": "contract_type", "path": "type", "type": "string"},
                {
                    "name": "contract_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class CoverageContractTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Coverage", "contract", VIEW_DEFINITION)
