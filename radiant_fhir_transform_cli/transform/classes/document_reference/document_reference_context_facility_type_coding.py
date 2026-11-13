"""FHIR DocumentReference context_facility_type_coding transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "DocumentReference",
    "name": "document_reference_context_facility_type_coding",
    "status": "active",
    "constant": [
        {
            "name": "id_hash",
            "valueString": "hash_row()",
        },
    ],
    "select": [
        {
            "column": [
                {
                    "name": "id",
                    "path": "%id_hash",
                    "type": "string",
                },
                {
                    "name": "document_reference_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "context.facilityType.coding",
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


class DocumentReferenceContextFacilityTypeCodingTransformer(FhirResourceTransformer):
    resource_type = "DocumentReference"
    resource_component = "context_facility_type_coding"
    view_definition = VIEW_DEFINITION
