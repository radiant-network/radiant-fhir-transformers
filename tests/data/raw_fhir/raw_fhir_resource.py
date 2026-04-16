RESOURCE = {
    "resourceType": "Observation",
    "id": "fUru66DnsInJJFSK0eHsjU8K8GtyH6pkh0LeyaSldORw4",
    "extension": [
        {
            "valueIdentifier": {
                "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.77777",
                "value": "887",
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/template-id",
        },
        {
            "valueIdentifier": {
                "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.707684",
                "value": "555",
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/template-id",
        },
    ],
    "identifier": [
        {
            "use": "official",
            "system": "http://www.bmc.nl/zorgportal/identifiers/observations",
            "value": "6326",
        }
    ],
    "basedOn": [
        {
            "reference": "ServiceRequest/eKSdPx93PPg7jLqFtgAKjJbL1RWvYEkyba5u.yiQaXZE3",
            "display": "Rapid SARS-CoV-2 PCR",
        },
        {
            "reference": "ServiceRequest/elkj;lskdjf;ljl;ghghhhddddddjj.yiQaXZE3",
            "display": "Rapid TESTER",
        },
    ],
    "partOf": [{"reference": "Procedure/procedure"}],
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory",
                }
            ],
            "text": "Laboratory",
        },
        {
            "coding": [
                {
                    "system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.798268.30",
                    "code": "lab",
                }
            ],
            "text": "Lab",
        },
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "94500-6",
                "display": "SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory system specimen by NAA with probe detection",
            },
            {
                "system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.600012",
                "code": "RCOVID",
            },
            {
                "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.768282",
                "code": "123090220",
                "display": "Rapid Sars-CoV-2",
            },
        ],
        "text": "Rapid Sars-CoV-2",
    },
    "subject": {
        "reference": "Patient/evrlLhFNe5BfHZQD39Kr9nfIA0e.TcZOdE0gOPoRXlGs3",
        "display": "CareEverywhere,Sammy",
    },
    "focus": [{"reference": "Condition/condition"}],
    "encounter": {
        "reference": "Encounter/e.mnIF2M9LQgwkDzhr2PCKA3",
        "display": "Hospital Encounter",
    },
    "effectiveDateTime": "2024-01-29T16:46:00Z",
    "issued": "2024-01-29T16:46:57Z",
    "performer": [
        {
            "reference": "Practitioner/erZ.j;lkj;lskdjfjffd",
            "display": "Sammy, Test",
        },
        {
            "reference": "Practitioner/erZ.abcdefg",
            "display": "Charlie, Tester",
        },
    ],
    "valueCodeableConcept": {
        "coding": [
            {"system": "http://snomed.info/sct_1", "code": "260415000"},
            {"system": "http://snomed.info/sct_2", "code": "9999999"},
            {"system": "http://snomed.info/sct_3", "code": "8888888"},
        ],
        "text": "Negative",
    },
    "dataAbsentReason": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/data-absent-reason",
                "code": "unknown",
                "display": "Unknown",
            }
        ]
    },
    "interpretation": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
                    "code": "NEG",
                    "display": "Negative",
                }
            ]
        }
    ],
    "specimen": {
        "reference": "Specimen/eofvi8EpxgTC9958OEt3Xuw3",
        "display": "Specimen 24U-ID-0290004",
    },
    "device": {"reference": "Device/device"},
    "referenceRange": [{"text": "Negative"}],
    "hasMember": [
        {"reference": "QuestionnaireResponse/questionnaire-response"}
    ],
    "derivedFrom": [{"reference": "DocumentReference/document-reference"}],
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8480-6",
                        "display": "Systolic blood pressure",
                    }
                ],
                "text": "Systolic blood pressure",
            },
            "valueRange": {
                "low": {"value": 2, "unit": "test"},
                "high": {"value": 6, "unit": "test"},
            },
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8462-4",
                        "display": "Diastolic blood pressure",
                    }
                ],
                "text": "Diastolic blood pressure",
            },
            "valueRange": {
                "low": {"value": 1, "unit": "test1"},
                "high": {"value": 3, "unit": "test1"},
            },
        },
    ],
}
