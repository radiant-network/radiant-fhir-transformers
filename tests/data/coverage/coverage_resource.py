RESOURCE = {
    "resourceType": "Coverage",
    "id": "9876B1",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable rendering of the coverage</div>',
    },
    "identifier": [
        {"system": "http://benefitsinc.com/certificate", "value": "12345"}
    ],
    "status": "active",
    "type": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": "EHCPOL",
                "display": "extended healthcare",
            }
        ]
    },
    "policyHolder": {"reference": "Organization/CBI35"},
    "subscriber": {"reference": "Patient/4"},
    "subscriberId": "CHOP12345678",
    "beneficiary": {"reference": "Patient/4"},
    "dependent": "0",
    "relationship": {"coding": [{"code": "self"}]},
    "period": {
        "start": "2011-05-23",
        "end": "2012-05-23",
    },
    "payor": [{"reference": "Organization/2"}],
    "class": [
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
                        "code": "group",
                    }
                ]
            },
            "value": "CB135",
            "name": "Corporate Baker's Inc. Local #35",
        },
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
                        "code": "subgroup",
                    }
                ]
            },
            "value": "123",
            "name": "Trainee Part-time Benefits",
        },
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/coverage-class",
                        "code": "plan",
                    }
                ]
            },
            "value": "B37FC",
            "name": "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC",
        },
    ],
    "order": 2,
    "network": "5",
    "costToBeneficiary": [
        {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/coverage-copay-type",
                        "code": "gpvisit",
                    }
                ]
            },
            "valueMoney": {"value": 20.0, "currency": "USD"},
            "exception": [
                {
                    "type": {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception",
                                "code": "retired",
                            }
                        ]
                    },
                    "period": {
                        "start": "2018-01-01",
                        "end": "2018-12-31",
                    },
                }
            ],
        }
    ],
    "subrogation": True,
    "contract": [{"reference": "Contract/INS-101"}],
}
