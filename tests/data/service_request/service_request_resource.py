RESOURCE = {
    "resourceType": "ServiceRequest",
    "id": "di_abcd_efg",
    "identifier": [
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "PLAC",
                    }
                ],
                "text": "Placer",
            },
            "system": "urn:oid:1.3.4.5.6.7",
            "value": "2345234234234",
        }
    ],
    "instantiatesUri": [{"value": "myurivalue.com"}],
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: di</p><p><b>status</b>: active</p><p><b>intent</b>: original-order</p><p><b>code</b>: Chest CT <span>(Details : {LOINC code '24627-2' = 'Chest CT)</span></p><p><b>subject</b>: <a>Patient/dicom</a></p><p><b>occurrence</b>: 08/05/2013 9:33:27 AM</p><p><b>requester</b>: <a>Dr. Adam Careful</a></p><p><b>reasonCode</b>: Check for metastatic disease <span>(Details )</span></p></div>",
    },
    "status": "active",
    "intent": "original-order",
    "priority": "routine",
    "replaces": [
        {
            "reference": "serviceRequest/banana",
            "display": "Previous allergy test",
        }
    ],
    "contained": [
        {
            "resourceType": "Observation",
            "id": "fasting",
            "status": "final",
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "49541-6",
                        "display": "Fasting status - Reported",
                    }
                ]
            },
            "subject": {"reference": "Patient/example"},
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0136",
                        "code": "Y",
                        "display": "Yes",
                    }
                ]
            },
        },
        {
            "resourceType": "Specimen",
            "id": "serum",
            "identifier": [
                {
                    "system": "http://acme.org/specimens",
                    "value": "20150107-0012",
                }
            ],
            "type": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "119364003",
                        "display": "Serum sample",
                    }
                ]
            },
            "subject": {"reference": "Patient/example"},
            "collection": {"collectedDateTime": "2015-08-16T06:40:17Z"},
        },
    ],
    "basedOn": [
        {
            "display": "ServiceRequest for Myringotomy and insertion of tympanic ventilation tube",
            "reference": "somereferencestring",
        }
    ],
    "code": {
        "coding": [{"system": "http://loinc.org", "code": "24627-2"}],
        "text": "Chest CT",
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "103696004",
                    "display": "Patient referral to specialist",
                }
            ]
        }
    ],
    "quantityQuantity": {
        "value": "5",
        "comparator": "something",
        "unit": "acres",
        "system": "imperial_units",
        "code": "konami",
    },
    "quantityRatio": {
        "numerator": {
            "value": 1,  # change this back to numeric.  Only switched to string so validation will pass
            "comparator": 5,
            "unit": "gallons",
            "system": "metric",
            "code": "gl",
        },
        "denominator": {
            "value": 2,
            "comparator": 5,
            "unit": "gallons",
            "system": "metric",
            "code": "gl",
        },
    },
    "quantityRange": {
        "low": {
            "value": 1,
            "unit": "part",
        },
        "high": {
            "value": 10,
            "unit": "part",
        },
    },
    "doNotPerform": True,
    "subject": {
        "reference": "Patient/dicom.example.pt",
        "display": "Judy Test",
    },
    "encounter": {"reference": "Encounter/example", "display": "1234encounter"},
    "insurance": [
        {"reference": "Coverage/abc-123", "display": "BCBS of Atlantis"}
    ],
    "locationCode": [{"text": "Pediatrics"}],
    "locationReference": [
        {"reference": "Location/zyx-vut", "display": "The Pitt"}
    ],
    "occurrenceDateTime": "2013-05-08T09:33:27+07:00",
    "occurrencePeriod": {
        "start": "2013-05-08",
        "end": "2013-05-09",
    },
    "orderDetail": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "243144002",
                    "display": "Patient triggered inspiratory assistance (procedure)",
                }
            ],
            "text": "IPPB",
        },
        {
            "text": " Initial Settings : Sens: -1 cm H20 Pressure 15 cm H2O moderate flow:  Monitor VS every 15 minutes x 4 at the start of mechanical ventilation, then routine for unit OR every 5 hr"
        },
    ],
    "occurrenceTiming": {
        "repeat": {
            "count": 20,
            "countMax": 30,
            "frequency": 3,
            "period": 1,
            "periodUnit": "wk",
        },
    },
    "requester": {
        "reference": "Practitioner/example.doc",
        "display": "Dr. Adam Careful",
    },
    "asNeededBoolean": False,
    "asNeededCodeableConcept": {
        "coding": [
            {
                "system": "http://mysystem.org",
                "code": "123-yes",
            },
        ],
        "text": "as needed text example",
    },
    "authoredOn": "2014-02-14",
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "90831000119105",
                    "display": "Check for metastatic disease",
                },
            ],
            "text": "Check for metastatic disease",
        }
    ],
    "performerType": {
        "coding": [
            {
                "system": "http://orionhealth.com/fhir/apps/specialties",
                "code": "ent",
                "display": "ENT",
            }
        ],
        "text": "Ear Nose and Throat",
    },
    "performer": [{"reference": "Practitioner/f202"}],
    "bodySite": [{"coding": [{"display": "Right arm"}], "text": "Right arm"}],
    "reasonReference": [{"display": "Patient has a spinal fracture"}],
    "relevantHistory": [
        {"reference": "#signature", "display": "Author's Signature"}
    ],
    "specimen": [{"reference": "#serum", "display": "Serum specimen"}],
    "supportingInfo": [{"reference": "#fasting", "display": "Fasting status"}],
    "patientInstruction": "Start with 30kg 10-15 repetitions for three sets and increase in increments of 5kg when you feel ready",
    "note": [
        {
            "authorString": "Serena Shrink",
            "time": "2014-02-14",
            "text": "patient is afraid of needles",
        }
    ],
}
