RESOURCE = {
    "resourceType": "DocumentReference",
    "id": "eGTI41.Isi638FTkMSoEA47L5.WtT25eJ-zlSghkBD543",
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
        "display": "JEK, Danger",
    },
    "date": "2021-10-27T19:02:27Z",
    "author": [
        {
            "reference": "Practitioner/emnkokS3ex3pMjlzS7Qtl7A3",
            "type": "Practitioner",
            "display": "Doctor Kay Jr.",
        }
    ],
    "custodian": {
        "identifier": {
            "system": "urn:ietf:rfc:3986",
            "value": "urn:epic:cec.idecur",
        }
    },
    "content": [
        {
            "attachment": {
                "contentType": "application/pdf",
                "url": "Binary/eNVo36G0dNhtI70LrZFsf725wDrfmnjA-ZAnqJA3AEv8V1lh.HzYSZ-maN9StcdvL3",
            }
        }
    ],
    "context": {
        "encounter": [
            {
                "identifier": {
                    "use": "usual",
                    "system": "urn:oid:1.2.840.114350.1.13.5325.1.7.3.698084.8",
                    "value": "10002444658",
                },
                "display": "Letter (Out)",
            }
        ],
        "period": {"start": "2021-04-03T17:25:00Z"},
    },
}
