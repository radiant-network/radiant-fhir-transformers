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
    "effectiveTiming": {
        "event": ["2024-01-29T16:46:00Z"],
        "repeat": {
            "dayOfWeek": ["mon"],
            "timeOfDay": ["16:46:00"],
            "when": ["HS"],
        },
        "code": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-GTSAbbreviation",
                    "code": "PM",
                    "display": "PM",
                }
            ]
        },
    },
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
    "note": [
        {
            "text": "This test was developed and its performance characteristics determined by the Children's Hospital of Philadelphia clinical laboratory. The U. S. Food and Drug Administration has not approved or cleared this test; however, FDA clearance or approval is not currently required for clinical use. The results are not intended to be used as the sole means of clinical diagnosis or patient management decisions. This laboratory is certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA-88) as qualified to perform high complexity clinical laboratory testing.\r\nThe 2019 novel coronavirus (SARS-CoV-2) target nucleic acids NOT DETECTED by real-time PCR.\r\n\r\nThis test was developed and its performance characteristics determined by Cepheid. This test has not been FDA cleared or approved. This test has been authorized by the FDA under an Emergency Use Authorization (EUA). This test is only authorized for the duration of time that circumstances exist justifying the authorization of the emergency use of in vitro diagnostic tests for detection of SARS-CoV-2 virus and/or diagnosis of COVID-19 infection under section 564(b)(1) of the Act, 21 U.S.C. 360bbb-3(b)(1), unless the authorization is terminated or revoked sooner. The Children's Hospital of Philadelphia is authorized to perform this test as certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA-88) as qualified to perform high complexity clinical laboratory testing. The results are not intended to be used as the sole means of clinical diagnosis or patient management decision."
        },
        {"text": "Test CHOP"},
    ],
    "bodySite": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "20139000",
                "display": "Structure of respiratory system (body structure)",
            }
        ]
    },
    "method": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "1240461000000109",
                "display": "Measurement of severe acute respiratory syndrome coronavirus 2 antibody (observable entity)",
            }
        ]
    },
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
