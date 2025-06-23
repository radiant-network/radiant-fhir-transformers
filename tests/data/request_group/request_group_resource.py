RESOURCE = {
    "resourceType": "RequestGroup",
    "id": "kdn5-example",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">Administer gemcitabine and carboplatin.</div>',
    },
    "identifier": [{"value": "requestgroup-kdn5"}],
    "instantiatesCanonical": ["PlanDefinition/KDN5"],
    "instantiatesUri": ["PlanDefinition/KDN5"],
    "basedOn": [{"reference": "MedicationRequest/medication-request"}],
    "replaces": [{"reference": "RequestGroup/request-group"}],
    "groupIdentifier": {
        "system": "http://example.org/treatment-group",
        "value": "00001",
    },
    "status": "draft",
    "intent": "plan",
    "priority": "routine",
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "18629005",
                "display": "Administration of drug or medicament (procedure)",
            }
        ]
    },
    "subject": {"reference": "Patient/example"},
    "encounter": {"reference": "Encounter/example"},
    "authoredOn": "2017-03-06T17:31:00Z",
    "author": {"reference": "Practitioner/1"},
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "363443007",
                    "display": "Malignant neoplasm of ovary (disorder)",
                }
            ]
        }
    ],
    "reasonReference": [{"reference": "Condition/condition"}],
    "note": [{"text": "Additional notes about the request group"}],
    "action": [
        {
            "prefix": "1",
            "title": "Administer Medications",
            "description": "Administer medications at the appropriate time",
            "textEquivalent": "Administer medication 1, followed an hour later by medication 2",
            "timingDateTime": "2017-03-06T19:00:00Z",
            "participant": [{"reference": "Practitioner/1"}],
            "groupingBehavior": "logical-group",
            "selectionBehavior": "all",
            "requiredBehavior": "must",
            "precheckBehavior": "yes",
            "cardinalityBehavior": "single",
            "action": [
                {
                    "id": "medication-action-1",
                    "description": "Administer medication 1",
                    "type": {"coding": [{"code": "create"}]},
                    "resource": {"reference": "#medicationrequest-1"},
                },
                {
                    "id": "medication-action-2",
                    "description": "Administer medication 2",
                    "relatedAction": [
                        {
                            "actionId": "medication-action-1",
                            "relationship": "after-end",
                            "offsetDuration": {"value": 1, "unit": "h"},
                        }
                    ],
                    "type": {"coding": [{"code": "create"}]},
                    "resource": {"reference": "#medicationrequest-2"},
                },
            ],
        }
    ],
}
