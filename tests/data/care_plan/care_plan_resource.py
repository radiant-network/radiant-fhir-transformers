RESOURCE = {
    "resourceType": "CarePlan",
    "id": "preg",
    "text": {
        "status": "additional",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">\n      <p>A maternity care plan (for a pregnant woman).</p>\n      <p>LMP is 1st Jan, 2013 (a great new years party!) The plan has activities to take prenatal vitamins, schedule first antenatal,\n            and 'placeholders' for the second antenatal and delivery (there would be lots of others of course)</p>\n      <p>Note that where is a proposed 'status' element against each activity</p>\n    </div>",
    },
    "contained": [
        {
            "resourceType": "Condition",
            "id": "p1",
            "clinicalStatus": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                        "code": "active",
                    }
                ]
            },
            "verificationStatus": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                        "code": "confirmed",
                    }
                ]
            },
            "code": {"text": "pregnancy"},
            "subject": {"reference": "Patient/1", "display": "Eve Everywoman"},
        },
        {
            "resourceType": "Practitioner",
            "id": "pr1",
            "name": [{"family": "Midwife", "given": ["Mavis"]}],
        },
        {
            "resourceType": "Practitioner",
            "id": "pr2",
            "name": [{"family": "Obstetrician", "given": ["Oscar"]}],
        },
        {
            "resourceType": "CareTeam",
            "id": "careteam",
            "participant": [
                {
                    "role": [
                        {
                            "coding": [
                                {
                                    "system": "http://example.org/mysys",
                                    "code": "lmc",
                                }
                            ],
                            "text": "Midwife",
                        }
                    ],
                    "member": {"reference": "#pr1", "display": "Mavis Midwife"},
                },
                {
                    "role": [
                        {
                            "coding": [
                                {
                                    "system": "http://example.org/mysys",
                                    "code": "obs",
                                }
                            ],
                            "text": "Obstretitian",
                        }
                    ],
                    "member": {
                        "reference": "#pr2",
                        "display": "Oscar Obstetrician",
                    },
                },
            ],
        },
        {
            "resourceType": "Goal",
            "id": "goal",
            "lifecycleStatus": "active",
            "description": {
                "text": "Maintain patient's health throughout pregnancy and ensure a healthy child"
            },
            "subject": {"reference": "Patient/1", "display": "Eve Everywoman"},
        },
    ],
    "extension": [
        {
            "url": "http://example.org/fhir/StructureDefinition/careplan#lmp",
            "valueDateTime": "2013-01-01",
        }
    ],
    "status": "active",
    "intent": "plan",
    "instantiatesUri": ["http://example.org/protocol-for-obesity"],
    "instantiatesCanonical": [
        "http://example.org/fhir/CarePlanDefinition/KDN5"
    ],
    "basedOn": [{"display": "Management of Type 2 Diabetes"}],
    "replaces": [{"display": "Plan from urgent care clinic"}],
    "partOf": [{"display": "Overall wellness plan"}],
    "category": [{"text": "Weight management plan"}],
    "contributor": {
        "reference": "Practitioner/example",
        "display": "Peter Example",
    },
    "identifier": [
        {
            "use": "official",
            "system": "http://www.bmc.nl/zorgportal/identifiers/careplans",
            "value": "CP2903",
        }
    ],
    "subject": {"reference": "Patient/1", "display": "Eve Everywoman"},
    "period": {"start": "2013-01-01", "end": "2013-10-01"},
    "careTeam": [{"reference": "#careteam"}],
    "addresses": [{"reference": "#p1", "display": "pregnancy"}],
    "supportingInfo": [{"reference": "#support", "display": "support"}],
    "goal": [{"reference": "#goal"}],
    "activity": [
        {"reference": {"display": "Prenatal vitamin MedicationRequest"}},
        {
            "extension": [
                {
                    "url": "http://example.org/fhir/StructureDefinition/careplan#andetails",
                    "valueUri": "http://orionhealth.com/fhir/careplan/1andetails",
                }
            ],
            "detail": {
                "kind": "Appointment",
                "code": {
                    "coding": [
                        {"system": "http://example.org/mySystem", "code": "1an"}
                    ],
                    "text": "First Antenatal encounter",
                },
                "status": "scheduled",
                "doNotPerform": False,
                "scheduledTiming": {
                    "repeat": {
                        "boundsPeriod": {
                            "start": "2013-02-14",
                            "end": "2013-02-28",
                        }
                    }
                },
                "performer": [
                    {"reference": "#pr1", "display": "Mavis Midwife"}
                ],
                "description": "The first antenatal encounter. This is where a detailed physical examination is performed.             and the pregnanacy discussed with the mother-to-be.",
            },
        },
        {
            "detail": {
                "kind": "Appointment",
                "code": {
                    "coding": [
                        {"system": "http://example.org/mySystem", "code": "an"}
                    ],
                    "text": "Follow-up Antenatal encounter",
                },
                "status": "not-started",
                "doNotPerform": False,
                "scheduledTiming": {
                    "repeat": {
                        "boundsPeriod": {
                            "start": "2013-03-01",
                            "end": "2013-03-14",
                        }
                    }
                },
                "performer": [
                    {"reference": "#pr1", "display": "Mavis Midwife"}
                ],
                "description": "The second antenatal encounter. Discuss any issues that arose from the first antenatal encounter",
            }
        },
        {
            "detail": {
                "kind": "Appointment",
                "code": {
                    "coding": [
                        {"system": "http://example.org/mySystem", "code": "del"}
                    ],
                    "text": "Delivery",
                },
                "status": "not-started",
                "doNotPerform": False,
                "scheduledTiming": {
                    "repeat": {
                        "boundsPeriod": {
                            "start": "2013-09-01",
                            "end": "2013-09-14",
                        }
                    }
                },
                "performer": [
                    {"reference": "#pr1", "display": "Mavis Midwife"}
                ],
                "description": "The delivery.",
            }
        },
    ],
    "note": [
        {
            "text": "Patient family is not ready to commit to goal setting at this time.  Goal setting will be addressed in the future",
            "time": "2014-02-14",
        }
    ],
}
