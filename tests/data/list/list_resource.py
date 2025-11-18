RESOURCE = {
    "resourceType": "List",
    "id": "med-list",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">\n      <p>Add hydroxocobalamin</p>\n      <p>Cancel Morphine Sulphate</p>\n    </div>',
    },
    "identifier": [
        {
            "system": "urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59",
            "value": "23974652",
        }
    ],
    "status": "current",
    "mode": "changes",
    "title": "Current Medication List",
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "182836005",
                "display": "Review of medication",
            }
        ],
        "text": "Medication Review",
    },
    "subject": {"reference": "Patient/example"},
    "encounter": {"reference": "Encounter/example"},
    "date": "2013-11-20T23:10:23+11:00",
    "source": {"reference": "Patient/example"},
    "emptyReason": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/list-empty-reason",
                "code": "nilknown",
                "display": "Nil Known",
            }
        ],
        "text": "The patient is not on any medications",
    },
    "orderedBy": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/list-order",
                "code": "entry-date",
            }
        ]
    },
    "note": [
        {
            "text": "Both parents, both brothers and both children (twin) are still alive."
        }
    ],
    "entry": [
        {
            "flag": {
                "coding": [
                    {
                        "system": "http://nehta.gov.au/codes/medications/changetype",
                        "code": "01",
                        "display": "Prescribed",
                    }
                ]
            },
            "deleted": False,
            "item": {
                "reference": "#fmh-1",
                "display": "hydroxocobalamin",
            },
        },
        {
            "flag": {
                "coding": [
                    {
                        "system": "http://nehta.gov.au/codes/medications/changetype",
                        "code": "02",
                        "display": "Cancelled",
                    }
                ]
            },
            "deleted": True,
            "item": {
                "reference": "#fmh-2",
                "display": "Morphine Sulfate",
            },
        },
    ],
}
