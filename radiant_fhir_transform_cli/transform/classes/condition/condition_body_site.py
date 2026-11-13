"""FHIR Condition body_site transformer"""

from radiant_fhir_transform_cli.transform.classes.base import (
    FhirResourceTransformer,
)

VIEW_DEFINITION = {
    "resource": "Condition",
    "name": "condition_body_site",
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
                    "name": "condition_id",
                    "path": "id",
                    "type": "string",
                },
            ],
        },
        {
            "forEachOrNull": "bodySite",
            "column": [
                {
                    "name": "body_site_coding",
                    "path": "coding",
                    "type": "string",
                    "collection": True,
                },
                {
                    "name": "body_site_text",
                    "path": "text",
                    "type": "string",
                },
            ],
        },
    ],
}


class ConditionBodySiteTransformer(FhirResourceTransformer):
    resource_type = "Condition"
    resource_component = "body_site"
    view_definition = VIEW_DEFINITION
