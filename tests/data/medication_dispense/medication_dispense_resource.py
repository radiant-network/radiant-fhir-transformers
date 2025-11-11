RESOURCE = {
    "resourceType": "MedicationDispense",
    "id": "meddisp001",
    "status": "in-progress",
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
    ]
}