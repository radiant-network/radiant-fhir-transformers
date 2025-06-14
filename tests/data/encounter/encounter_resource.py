RESOURCE = {
    "resourceType": "Encounter",
    "id": "f203",
    "identifier": [{"use": "temp", "value": "Encounter_Roel_20130311"}],
    "status": "finished",
    "statusHistory": [{"status": "arrived", "period": {"start": "2013-03-08"}}],
    "class": {
        "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
        "code": "IMP",
        "display": "inpatient encounter",
    },
    "classHistory": [
        {
            "class": {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": "IMP",
                "display": "inpatient encounter",
            },
            "period": {
                "start": "2013-03-08T00:00:00Z",
                "end": "2013-03-08T00:00:00Z",
            },
        }
    ],
    "type": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "183807002",
                    "display": "Inpatient stay for nine days",
                }
            ]
        }
    ],
    "serviceType": {
        "coding": [
            {
                "display": "test",
            }
        ],
        "text": "test",
    },
    "priority": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "394849002",
                "display": "High priority",
            }
        ]
    },
    "subject": {"reference": "Patient/f201", "display": "Roel"},
    "episodeOfCare": [{"reference": "EpisodeOfCare/example"}],
    "basedOn": [{"reference": "ServiceRequest/myringotomy"}],
    "participant": [
        {
            "type": [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                            "code": "PART",
                        }
                    ]
                }
            ],
            "individual": {"reference": "Practitioner/f201"},
        }
    ],
    "appointment": [{"reference": "Appointment/example"}],
    "period": {"start": "2013-03-11", "end": "2013-03-20"},
    "reasonCode": [
        {
            "text": "The patient seems to suffer from bilateral pneumonia and renal insufficiency, most likely due to chemotherapy."
        }
    ],
    "reasonReference": [{"reference": "Condition/example"}],
    "diagnosis": [
        {
            "condition": {"reference": "Condition/stroke"},
            "use": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                        "code": "AD",
                        "display": "Admission diagnosis",
                    }
                ]
            },
            "rank": 1,
        },
        {
            "condition": {"reference": "Condition/f201"},
            "use": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                        "code": "DD",
                        "display": "Discharge diagnosis",
                    }
                ]
            },
        },
    ],
    "account": [{"reference": "Account/example"}],
    "hospitalization": {
        "origin": {"reference": "Location/2"},
        "admitSource": {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "309902002",
                    "display": "Clinical Oncology Department",
                }
            ]
        },
        "reAdmission": {"coding": [{"display": "readmitted"}]},
        "dietPreference": [
            {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "276026009",
                        "display": "Fluid balance regulation",
                    }
                ]
            }
        ],
        "specialCourtesy": [
            {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v3-EncounterSpecialCourtesy",
                        "code": "NRM",
                        "display": "normal courtesy",
                    }
                ]
            }
        ],
        "specialArrangement": [
            {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/encounter-special-arrangements",
                        "code": "wheel",
                        "display": "Wheelchair",
                    }
                ]
            }
        ],
        "destination": {"reference": "Location/2"},
    },
    "location": [
        {
            "location": {"display": "Example"},
            "status": "active",
            "period": {
                "start": "2017-02-01T07:15:00+10:00",
                "end": "2017-02-01T08:45:00+10:00",
            },
        }
    ],
    "serviceProvider": {"reference": "Organization/2"},
    "partOf": {"reference": "Encounter/f203"},
}
