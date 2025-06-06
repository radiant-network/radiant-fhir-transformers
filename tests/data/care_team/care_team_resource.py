RESOURCE = {
    "resourceType": "CareTeam",
    "id": "example",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">Care Team</div>',
    },
    "contained": [
        {
            "resourceType": "Practitioner",
            "id": "pr1",
            "name": [{"family": "Dietician", "given": ["Dorothy"]}],
        }
    ],
    "identifier": [{"value": "12345"}],
    "status": "active",
    "category": [
        {
            "coding": [
                {
                    "system": "http://loinc.org",
                    "code": "LA27976-2",
                    "display": "Encounter-focused care team",
                }
            ]
        }
    ],
    "name": "Peter James Charlmers Care Plan for Inpatient Encounter",
    "subject": {
        "reference": "Patient/example",
        "display": "Peter James Chalmers",
    },
    "encounter": {"reference": "Encounter/example"},
    "period": {"end": "2013-01-01"},
    "participant": [
        {
            "role": [{"text": "responsiblePerson"}],
            "member": {
                "reference": "Patient/example",
                "display": "Peter James Chalmers",
            },
        },
        {
            "role": [{"text": "adviser"}],
            "member": {
                "reference": "Practitioner/pr1",
                "display": "Dorothy Dietition",
            },
            "onBehalfOf": {"reference": "Organization/f001"},
            "period": {"end": "2013-01-01"},
        },
    ],
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "400097005",
                    "display": "Ingrowing nail",
                }
            ],
            "text": "Ingrowing nail",
        }
    ],
    "reasonReference": [
        {
            "reference": "Condition/reason",
            "type": "Condition",
            "display": "The justification that the procedure was performed",
        }
    ],
    "managingOrganization": [{"reference": "Organization/f001"}],
    "telecom": [
        {"system": "phone", "value": "215-590-3326", "use": "work"},
        {"system": "fax", "value": "215-590-3606", "use": "work"},
    ],
    "note": [
        {
            "text": "Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding."
        }
    ],
}
