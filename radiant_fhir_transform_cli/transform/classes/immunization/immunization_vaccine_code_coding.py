"""FHIR Immunization vaccine_code_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_vaccine_code_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {"name": "immunization_id", "path": "id", "type": "string"},
            ]
        },
        {
            "forEach": "vaccineCode.coding",
            "column": [
                {
                    "name": "vaccine_code_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "vaccine_code_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "vaccine_code_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class ImmunizationVaccineCodeCodingTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "vaccine_code_coding", VIEW_DEFINITION)
