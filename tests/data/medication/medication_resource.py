RESOURCE = {
    "resourceType": "Medication",
    "id": "med0301",
    "identifier": [
        {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698288",
            "value": "21279",
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://hl7.org/fhir/sid/ndc",
                "code": "0069-2587-10",
                "display": "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)",
            }
        ],
        "text": "Vancomycin HCL",
    },
    "status": "active",
    "manufacturer": {
        "reference": "#org4",
        "type": "Organization",
        "display": "Organization 4",
    },
    "form": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "385219001",
                "display": "Conventional release solution for injection (dose form)",
            }
        ],
        "text": "Solution for injection",
    },
    "ingredient": [
        {
            "itemCodeableConcept": {
                "coding": [
                    {
                        "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                        "code": "66955",
                        "display": "Vancomycin Hydrochloride",
                    }
                ]
            },
            "isActive": True,
            "strength": {
                "numerator": {
                    "value": 500,
                    "system": "http://unitsofmeasure.org",
                    "code": "mg",
                },
                "denominator": {
                    "value": 10,
                    "system": "http://unitsofmeasure.org",
                    "code": "mL",
                },
            },
        }
    ],
    "batch": {"lotNumber": "9494788", "expirationDate": "2017-05-22"},
}
