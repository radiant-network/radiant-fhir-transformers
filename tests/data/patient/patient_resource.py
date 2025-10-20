RESOURCE = {
    "resourceType": "Patient",
    "id": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
    "extension": [
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.698084.130.657370.8551999258",
                        "code": "Female",
                        "display": "Female",
                    }
                ]
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/legal-sex",
        },
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.698084.130.657370.8551999258",
                        "code": "Female",
                        "display": "Female",
                    }
                ]
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/sex-for-clinical-use",
        },
        {
            "extension": [
                {
                    "valueCoding": {
                        "system": "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
                        "code": "UNK",
                        "display": "Unknown",
                    },
                    "url": "ombCategory",
                },
                {"valueString": "Unknown", "url": "text"},
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
        },
        {
            "extension": [{"valueString": "Unknown", "url": "text"}],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
        },
        {
            "valueCode": "248152002",
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-sex",
        },
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "LA29519-8",
                        "display": "she/her/her/hers/herself",
                    }
                ]
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/calculated-pronouns-to-use-for-text",
        },
    ],
    "identifier": [
        {
            "use": "usual",
            "type": {"text": "CEID"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.688884.100",
            "value": "CP2VXPJ1R6VX4LG",
        },
        {
            "use": "usual",
            "type": {"text": "EPI"},
            "system": "urn:oid:2.16.840.7.740741.2",
            "value": "82001496",
        },
        {
            "use": "usual",
            "type": {"text": "EXTERNAL"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698084",
            "value": "Z8201491",
        },
        {
            "use": "usual",
            "type": {"text": "FHIR"},
            "system": "http://open.epic.com/FHIR/StructureDefinition/patient-dstu2-fhir-id",
            "value": "Tu46VewHQTgHXc3sFCHUHh4O.MtOYlDMts1gZ9ximNigB",
        },
        {
            "use": "usual",
            "type": {"text": "FHIR STU3"},
            "system": "http://open.epic.com/FHIR/StructureDefinition/patient-fhir-id",
            "value": "e.YgoDNAQq8oI3tDG15j9MgilHSfub5QZZlVysqken6o3",
        },
        {
            "use": "usual",
            "type": {"text": "INTERNAL"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698084",
            "value": "Z8201491",
        },
        {
            "use": "usual",
            "type": {"text": "MYCHARTLOGIN"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.878082.110",
            "value": "BETTY123",
        },
        {
            "use": "usual",
            "type": {"text": "WPRINTERNAL"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.878082",
            "value": "482",
        },
        {
            "use": "usual",
            "system": "https://open.epic.com/FHIR/StructureDefinition/PayerMemberId",
            "value": "JKADJD",
        },
        {
            "use": "usual",
            "system": "urn:oid:2.16.840.1.113883.4.1",
            "_value": {
                "extension": [
                    {
                        "valueString": "xxx-xx-xxxx",
                        "url": "http://hl7.org/fhir/StructureDefinition/rendered-value",
                    }
                ]
            },
        },
    ],
    "active": True,
    "name": [
        {
            "use": "official",
            "text": "Betty MyChart",
            "family": "MyChart",
            "given": ["Betty"],
        },
        {
            "use": "usual",
            "text": "Betty MyChart",
            "family": "MyChart",
            "given": ["Betty"],
        },
        {
            "use": "old",
            "text": "MYCHARTADMIN,BETTY",
            "family": "Mychartadmin",
            "given": ["Betty"],
        },
    ],
    "telecom": [
        {
            "system": "phone",
            "value": "610-357-7956",
            "use": "mobile",
            "rank": 1,
        },
        {"system": "email", "value": "hakp@email.chop.edu", "rank": 1},
    ],
    "gender": "Female",
    "birthDate": "2010-02-03",
    "deceasedBoolean": False,
    "address": [
        {
            "use": "home",
            "line": ["1234 Administration Blvd"],
            "city": "SOUTHAMPTON",
            "district": "Bucks",
            "state": "PA",
            "postalCode": "18966",
            "country": "US",
        },
        {
            "use": "old",
            "line": ["1234 Adminsutration Blvd"],
            "city": "SOUTHAMPTON",
            "district": "Bucks",
            "state": "PA",
            "postalCode": "18966",
            "country": "US",
        },
        {
            "use": "old",
            "line": ["1234 Administration Blvd"],
            "city": "SOUTHAMPTON",
            "district": "Bucks",
            "state": "PA",
            "postalCode": "18966",
            "country": "US",
        },
    ],
    "maritalStatus": {"text": "Single"},
    "photo": [
        {
            "contentType": "image/gif",
            "url": "http://someimage.com",
        }
    ],
    "contact": [
        {
            "relationship": [
                {
                    "coding": [
                        {
                            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
                            "code": "3",
                            "display": "Father",
                        }
                    ],
                    "text": "Father",
                }
            ],
            "name": {"use": "usual", "text": "Dad1stName LastName"},
            "telecom": [
                {"system": "phone", "value": "215-777-7777", "use": "home"},
                {"system": "phone", "value": "215-888-8888", "use": "work"},
                {"system": "phone", "value": "215-444-4444", "use": "mobile"},
                {"system": "email", "value": "mychart@yahoo.com"},
            ],
            "address": {
                "use": "home",
                "line": ["1234 Administration Blvd"],
                "city": "SOUTHAMPTON",
                "district": "Bucks",
                "state": "PA",
                "postalCode": "18966",
                "country": "US",
            },
            "period": {"start": "2022-03-09"},
        }
    ],
    "communication": [
        {
            "language": {
                "coding": [
                    {
                        "system": "urn:ietf:bcp:47",
                        "code": "en",
                        "display": "English",
                    }
                ],
                "text": "English",
            },
            "preferred": True,
        }
    ],
    "generalPractitioner": [
        {
            "reference": "Practitioner/eGHJaqroQFAsUO8lEm-zIFw3",
            "type": "Practitioner",
            "display": "Kathleen O Crocker, MD",
        }
    ],
    "managingOrganization": {
        "reference": "Organization/e-ivxFMnjqfWfW4GruG953g3",
        "display": "Children's Hospital of Philadelphia",
    },
    "link": [
        {"other": {"reference": "Patient/pat2"}, "type": "seealso"},
        {"other": {"reference": "Patient/pat3"}, "type": "seealso1"},
    ],
}
