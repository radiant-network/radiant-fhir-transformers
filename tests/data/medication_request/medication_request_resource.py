RESOURCE = {
    "resourceType": "MedicationRequest",
    "id": "euHtu0fIBKsu8UhaYJaWMfg3",
    "meta": {
        "profile": [
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest"
        ]
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/medicationrequest-category",
                    "code": "Inpatient",
                    "display": "Inpatient",
                }
            ],
            "text": "Inpatient",
        }
    ],
    "status": "active",
    "intent": "order",
    "reportedBoolean": True,
    "medicationCodeableConcept": {
        "coding": [
            {
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": "1187314",
                "display": "Tylenol PM Pill",
            }
        ],
        "text": "Tylenol PM Pill",
    },
    "medicationReference": {
        "reference": "Medication/uscore-med2",
        "display": "Nizatidine 15 MG/ML Oral Solution [Axid]",
    },
    "subject": {"reference": "Patient/example", "display": "Amy Shaw"},
    "authoredOn": "2008-04-05",
    "encounter": {
        "reference": "Encounter/example-1",
        "display": "Office Visit",
    },
    "requester": {
        "reference": "Practitioner/practitioner-1",
        "display": "Ronald Bone, MD",
    },
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "version": "http://snomed.info/sct/731000124108",
                    "code": "25064002",
                    "display": "Headache (finding)",
                }
            ],
            "text": "Headache",
        }
    ],
    "reasonReference": [
        {
            "reference": "Condition/condition-duodenal-ulcer",
            "display": "Active Duodenal Ulcer",
        }
    ],
    "dosageInstruction": [
        {
            "text": "10 mL bid",
            "timing": {
                "code": {"text": "Every visit"},
                "repeat": {
                    "boundsPeriod": {"start": "2008-04-05"},
                    "frequency": 2,
                    "period": 1,
                    "periodUnit": "d",
                },
            },
            "doseAndRate": [
                {
                    "doseQuantity": {
                        "value": 10,
                        "unit": "ml",
                        "system": "http://unitsofmeasure.org",
                        "code": "mL",
                    }
                }
            ],
        }
    ],
    "dispenseRequest": {
        "numberOfRepeatsAllowed": 1,
        "quantity": {
            "value": 480,
            "unit": "mL",
            "system": "http://unitsofmeasure.org",
            "code": "mL",
        },
    },
}
