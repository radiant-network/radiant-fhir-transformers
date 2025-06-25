RESOURCE = {
    "resourceType": "DocumentReference",
    "id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
    "masterIdentifier": {
        "system": "urn:ietf:rfc:3986",
        "value": "urn:oid:129.6.58.92.88336",
    },
    "identifier": [
        {
            "system": "urn:oid:1.2.840.114350.1.13.5325.1.7.2.727879",
            "value": "1010618052",
        },
        {
            "system": "urn:oid:1.2.840.114350.1.72.3.15",
            "value": "1.2.840.114350.1.13.5325.1.7.2.727879_1010618052",
        },
    ],
    "status": "current",
    "docStatus": "preliminary",
    "type": {
        "coding": [
            {
                "system": "urn:oid:1.2.840.114350.1.13.5325.1.7.4.737880.5010",
                "code": "1",
                "display": "Progress Notes",
            },
            {
                "system": "urn:oid:1.2.840.114350.1.72.727879.69848980",
                "code": "1",
                "display": "Progress Notes",
            },
            {
                "system": "http://loinc.org",
                "code": "11506-3",
                "display": "Progress note",
                "userSelected": True,
            },
            {
                "system": "http://loinc.org",
                "code": "75492-9",
                "display": "Risk assessment and screening note",
            },
        ],
        "text": "Progress Notes",
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://hl7.org/fhir/us/core/CodeSystem/us-core-documentreference-category",
                    "code": "clinical-note",
                    "display": "Clinical Note",
                }
            ],
            "text": "Clinical Note",
        }
    ],
    "subject": {
        "reference": "Patient/eiCbDCEzFk6wR6UNlcWziySVQrlN47NTRvxPwgT4P3883",
    },
    "date": "2004-12-23",
    "author": [{"reference": "Practitioner/emnkokS3ex3pMjlzS7Qtl7A3"}],
    "authenticator": {"reference": "Organization/f001"},
    "custodian": {"reference": "Organization/custodian"},
    "relatesTo": [
        {
            "code": "appends",
            "target": {
                "reference": "DocumentReference/example",
            },
        }
    ],
    "securityLabel": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality",
                    "code": "N",
                    "display": "normal",
                }
            ]
        }
    ],
    "content": [
        {
            "attachment": {
                "contentType": "application/hl7-v3+xml",
                "language": "en-US",
                "url": "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510",
                "size": 3654,
                "hash": "2jmj7l5rSw0yVb/vlWAYkK/YBwk=",
                "title": "Physical",
                "creation": "2004-12-23",
            },
            "format": {
                "system": "urn:oid:1.3.6.1.4.1.19376.1.2.3",
                "code": "urn:ihe:pcc:handp:2008",
                "display": "History and Physical Specification",
            },
        }
    ],
    "context": {
        "encounter": [{"reference": "Encounter/xcda"}],
        "event": [
            {
                "coding": [
                    {
                        "system": "http://ihe.net/xds/connectathon/eventCodes",
                        "code": "T-D8200",
                        "display": "Arm",
                    }
                ]
            }
        ],
        "period": {
            "start": "2004-12-23",
            "end": "2004-12-23",
        },
        "facilityType": {
            "coding": [
                {
                    "system": "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes",
                    "code": "Outpatient",
                    "display": "Outpatient",
                }
            ]
        },
        "practiceSetting": {
            "coding": [
                {
                    "system": "http://www.ihe.net/xds/connectathon/practiceSettingCodes",
                    "code": "General Medicine",
                    "display": "General Medicine",
                }
            ]
        },
        "sourcePatientInfo": {"reference": "Patient/xcda"},
        "related": [{"reference": "Patient/xcda"}],
    },
}
