"""FHIR DocumentReference context_facility_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)


VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_context_facility_type_coding",
    "status": "active",
    "constant": [{"name": "id_uuid", "valueString": "uuid()"}],
    "select": [
        {
            "column": [
                {"name": "id", "path": "%id_uuid", "type": "string"},
                {
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ]
        },
        {
            "forEach": "context.facilityType.coding",
            "column": [
                {
                    "name": "context_facility_type_coding_system",
                    "path": "system",
                    "type": "string",
                },
                {
                    "name": "context_facility_type_coding_code",
                    "path": "code",
                    "type": "string",
                },
                {
                    "name": "context_facility_type_coding_display",
                    "path": "display",
                    "type": "string",
                },
            ],
        },
    ],
}


class DocumentReferenceContextFacilityTypeCodingTransformer(
    FhirResourceTransformer
):
    def __init__(self):
        super().__init__(
            "DocumentReference", "context_facility_type_coding", VIEW_DEFINITION
        )
