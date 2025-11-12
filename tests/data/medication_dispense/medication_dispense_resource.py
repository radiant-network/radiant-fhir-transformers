RESOURCE = {
    "resourceType": "MedicationDispense",
    "id": "meddisp001",
    "identifier": [
        {
            "use": "official",
            "system": "http://www.bmc.nl/portal/prescriptions",
            "value": "12345689",
        }
    ],
     "partOf": [
        {
        "reference": "Procedure/f001"
        }
    ],
    "status": "in-progress",
    "statusReasonCodeableConcept": {
        "coding": [
        {
            "system": "http://terminology.hl7.org/CodeSystem/medicationdispense-status-reason",
            "code": "refused",
            "display": "Refused"
        }
        ]
    },
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/medicationdispense-category",
                    "code": "inpatient",
                    "display": "Inpatient",
                }
            ],
            "text": "Requests for medications in inpatient or acute care settings",
        }
    ],
    "medicationCodeableConcept": {
        "coding": [
        {
            "system": "http://hl7.org/fhir/sid/ndc",
            "code": "76388-713-25",
            "display": "Myleran 2mg tablet, film coated"
        }
        ]
    },
    "medicationReference": {
        "reference": "#med0301",
        "display": "Vancomycin Hydrochloride"
    },
    "subject": {
        "reference": "Patient/pat1",
        "display": "Donald Duck"
    },
    "supportingInformation": [
        {
        "reference": "Condition/f203"
        }
    ],
    "performer": [
        {
        "actor": {
            "reference": "Practitioner/f006"
        }
        }
    ],
    "location": {
        "reference": "Location/ukp",
        "display": "Pharmacy"
    },
    "authorizingPrescription": [
        {
        "reference": "MedicationRequest/medrx0318"
        }
    ],
    "type": {
        "coding": [
        {
            "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
            "code": "EM",
            "display": "Emergency Supply"
        }
        ]
    },
    "quantity": {
        "value": 12,
        "unit": "Vial",
        "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
        "code": "Vial"
    },
    "daysSupply": {
        "value": 3,
        "unit": "Day",
        "system": "http://unitsofmeasure.org",
        "code": "d"
    },
    "whenPrepared": "2015-01-15T10:20:00Z",
    "destination": {
        "reference": "Location/ph"
    },
    "receiver": [
        {
        "reference": "Patient/pat1",
        "display": "Donald Duck"
        }
    ],
    "note": [{"text": "Patient told to take with food"}],
    "dosageInstruction": [
        {
        "sequence": 1,
        "text": "500mg IV q6h x 3 days",
        "timing": {
            "repeat": {
            "frequency": 1,
            "period": 6,
            "periodUnit": "h"
            }
        },
        "route": {
            "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "255560000",
                "display": "Intravenous"
            }
            ]
        },
        "method": {
            "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "420620005",
                "display": "Push - dosing instruction imperative (qualifier value)"
            }
            ]
        },
        "doseAndRate": [
            {
            "type": {
                "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/dose-rate-type",
                    "code": "ordered",
                    "display": "Ordered"
                }
                ]
            },
            "doseQuantity": {
                "value": 500,
                "unit": "mg",
                "system": "http://unitsofmeasure.org",
                "code": "mg"
            }
            }
        ]
        }
    ],
    "substitution": {
        "type": {
            "coding": [
                {
                "system": "http://terminology.hl7.org/CodeSystem/medicationdispense-category",
                "code": "inpatient",
                "display": "Inpatient"
                }
            ]
        },
        "reason": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "394802001",
                    "display": "Patient allergic to penicillin"
                }
            ],
            "text": "Patient allergic to penicillin"
        }
        ],
        "responsibleParty": [
        {
            "reference": "Practitioner/f007"
        }
        ]
    },
    "detectedIssue": [{"reference": "DetectedIssue/allergy"}],
    "eventHistory": [
        {"reference": "#signature", "display": "Author's Signature"}
    ],
}