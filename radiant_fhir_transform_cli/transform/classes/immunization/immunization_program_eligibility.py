"""FHIR Immunization program_eligibility transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "Immunization",
    "name": "immunization_program_eligibility",
    "status": "active",
    "constant": [
        {
            "name": "id_uuid",
            "valueString": "uuid()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_uuid",
                    "type": "string",
                },
                {
                    "name": "immunization_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEach": "programEligibility",
            "column": [
                {
                    "name": "program_eligibility_text",
                    "path": "text",
                    "type": "string",
                },
            ],
            "select": [
                {
                    "forEach": "coding",
                    "column": [
                        {
                            "name": "program_eligibility_coding_system",
                            "path": "system",
                            "type": "string",
                        },
                        {
                            "name": "program_eligibility_coding_code",
                            "path": "code",
                            "type": "string",
                        },
                    ],
                },
            ],
        },
    ],
}


class ImmunizationProgramEligibilityTransformer(FhirResourceTransformer):
    def __init__(self):
        super().__init__("Immunization", "program_eligibility", VIEW_DEFINITION)
