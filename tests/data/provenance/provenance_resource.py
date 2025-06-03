RESOURCE = {
    "resourceType": "Provenance",
    "id": "provenance",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">procedure record authored on 27-June 2015 by Harold Hippocrates, MD Content extracted from XDS managed CDA Referral received 26-June as authorized by a referenced Consent.</div>',
    },
    "target": [{"reference": "Procedure/target"}],
    "occurredPeriod": {"start": "2015-06-27", "end": "2015-06-28"},
    "recorded": "2015-06-27T08:39:24+10:00",
    "policy": ["http://acme.com/fhir/Consent/25"],
    "location": {"reference": "Location/location"},
    "reason": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "3457005",
                    "display": "Referral",
                }
            ]
        }
    ],
    "activity": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion",
                "code": "AU",
                "display": "authenticated",
            }
        ]
    },
    "agent": [
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                        "code": "AUT",
                    }
                ]
            },
            "who": {"reference": "Practitioner/author"},
        },
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                        "code": "DEV",
                    }
                ]
            },
            "who": {"reference": "Device/device"},
        },
    ],
    "entity": [
        {
            "role": "source",
            "what": {
                "reference": "DocumentReference/entity",
                "display": "CDA Document in XDS repository",
            },
        }
    ],
    "signature": [
        {
            "type": [
                {
                    "system": "urn:iso-astm:E1762-95:2013",
                    "code": "1.2.840.10065.1.12.1.5",
                    "display": "Verification Signature",
                }
            ],
            "when": "2015-08-27T08:39:24+10:00",
            "who": {"reference": "Practitioner/signature"},
            "targetFormat": "application/fhir+xml",
            "sigFormat": "application/signature+xml",
            "data": "Li4u",
        }
    ],
}
