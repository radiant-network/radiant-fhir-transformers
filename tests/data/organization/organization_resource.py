RESOURCE = {
    "resourceType": "Organization",
    "id": "2.16.840.1.113883.19.5",
    "identifier": [
        {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.8553241",
            "value": "7968",
        },
        {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.8553242",
            "value": "PH0453",
        },
        {
            "use": "usual",
            "type": {"text": "NPI"},
            "system": "http://hl7.org/fhir/sid/us-npi",
            "value": "1215921457",
        },
    ],
    "active": True,
    "type": [
        {
            "coding": [
                {
                    "system": "urn:oid:2.16.840.1.113883.2.4.15.1060",
                    "code": "V6",
                    "display": "University Medical Hospital",
                },
                {
                    "system": "http://terminology.hl7.org/CodeSystem/organization-type",
                    "code": "prov",
                    "display": "Healthcare Provider",
                },
            ]
        }
    ],
    "name": "Endoscopy Suite",
    "alias": ["ENS"],
    "telecom": [
        {"system": "phone", "value": "215-590-3326", "use": "work"},
        {"system": "fax", "value": "215-590-3606", "use": "work"},
    ],
    "address": [
        {
            "line": [
                "3401 Civic Center Boulevard",
                "Children's Hospital of Phila",
            ],
            "city": "Philadelphia",
            "state": "Pennsylvania",
            "postalCode": "19104",
            "country": "United States",
        }
    ],
    "partOf": {
        "reference": "Organization/eJeQyznJlo20Edf4V.q.Jwg3",
        "display": "CHILDREN'S HOSPITAL OF PHILADELPHIA RL",
    },
    "contact": [
        {
            "purpose": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
                        "code": "PRESS",
                    }
                ]
            },
            "telecom": [{"system": "phone", "value": "022-655 2334"}],
        },
        {
            "purpose": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
                        "code": "PATINF",
                    }
                ]
            },
            "telecom": [{"system": "phone", "value": "022-655 2335"}],
        },
    ],
    "endpoint": [{"reference": "Endpoint/endpoint"}],
}
