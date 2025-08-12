RESOURCE = {
    "resourceType": "MedicationRequest",
    "id": "medrx0301",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: medrx0301</p><p><b>contained</b>: , </p><p><b>identifier</b>: 12345689 (OFFICIAL)</p><p><b>status</b>: completed</p><p><b>statusReason</b>: Try another treatment first <span>(Details : {http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason code 'altchoice' = 'Try another treatment first', given as 'Try another treatment first'})</span></p><p><b>intent</b>: order</p><p><b>category</b>: Inpatient <span>(Details : {http://terminology.hl7.org/CodeSystem/medicationrequest-category code 'inpatient' = 'Inpatient', given as 'Inpatient'})</span></p><p><b>medication</b>: id: med0310; Oral Form Oxycodone (product) <span>(Details : {SNOMED CT code '430127000' = 'Oral form oxycodone', given as 'Oral Form Oxycodone (product)'})</span></p><p><b>subject</b>: <a>Donald Duck</a></p><p><b>encounter</b>: <a>encounter who leads to this prescription</a></p><p><b>supportingInformation</b>: <a>Procedure/biopsy</a></p><p><b>authoredOn</b>: 15/01/2015</p><p><b>requester</b>: <a>Patrick Pump</a></p><p><b>performer</b>: <a>Carla Espinosa</a></p><p><b>performerType</b>: Public Health Nurse <span>(Details : {SNOMED CT code '26369006' = 'Public health nurse', given as 'Public Health Nurse'})</span></p><p><b>reasonCode</b>: Rib Pain (finding) <span>(Details : {SNOMED CT code '297217002' = 'Rib pain', given as 'Rib Pain (finding)'})</span></p><p><b>insurance</b>: <a>Coverage/9876B1</a></p><p><b>note</b>: Patient told to take with food</p><p><b>dosageInstruction</b>: </p><h3>DispenseRequests</h3><table><tr><td>-</td><td><b>ValidityPeriod</b></td><td><b>NumberOfRepeatsAllowed</b></td><td><b>Quantity</b></td><td><b>ExpectedSupplyDuration</b></td><td><b>Performer</b></td></tr><tr><td>*</td><td>15/01/2015 --&gt; 15/01/2016</td><td>0</td><td>30 TAB<span> (Details: http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm code TAB = 'Tablet')</span></td><td>10 days<span> (Details: UCUM code d = 'd')</span></td><td><a>Practitioner/f001</a></td></tr></table><h3>Substitutions</h3><table><tr><td>-</td><td><b>Allowed[x]</b></td><td><b>Reason</b></td></tr><tr><td>*</td><td>true</td><td>formulary policy <span>(Details : {http://terminology.hl7.org/CodeSystem/v3-ActReason code 'FP' = 'formulary policy', given as 'formulary policy'})</span></td></tr></table><p><b>detectedIssue</b>: <a>DetectedIssue/allergy</a></p><p><b>eventHistory</b>: Author's Signature. Generated Summary: id: signature; recorded: 01/02/2017 5:23:07 PM; </p></div>",
    },
    "contained": [
        {
            "resourceType": "Medication",
            "id": "med0310",
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "430127000",
                        "display": "Oral Form Oxycodone (product)",
                    }
                ]
            },
        },
        {
            "resourceType": "Provenance",
            "id": "signature",
            "target": [{"reference": "ServiceRequest/physiotherapy"}],
            "recorded": "2017-02-01T17:23:07Z",
            "agent": [
                {
                    "role": [
                        {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                                    "code": "AUT",
                                }
                            ]
                        }
                    ],
                    "who": {
                        "reference": "Practitioner/example",
                        "display": "Dr Adam Careful",
                    },
                }
            ],
            "signature": [
                {
                    "type": [
                        {
                            "system": "urn:iso-astm:E1762-95:2013",
                            "code": "1.2.840.10065.1.12.1.1",
                            "display": "Author's Signature",
                        }
                    ],
                    "when": "2017-02-01T17:23:07Z",
                    "who": {
                        "reference": "Practitioner/example",
                        "display": "Dr Adam Careful",
                    },
                    "targetFormat": "application/fhir+xml",
                    "sigFormat": "application/signature+xml",
                    "data": "dGhpcyBibG9iIGlzIHNuaXBwZWQ=",
                }
            ],
        },
    ],
    "identifier": [
        {
            "use": "official",
            "system": "http://www.bmc.nl/portal/prescriptions",
            "value": "12345689",
        }
    ],
    "status": "completed",
    "statusReason": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason",
                "code": "altchoice",
                "display": "Try another treatment first",
            }
        ],
        "text": "This therapy is a backup and will be used only if the preferred therapy fails.",
    },
    "intent": "order",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/medicationrequest-category",
                    "code": "inpatient",
                    "display": "Inpatient",
                }
            ],
            "text": "Requests for medications in inpatient or acute care settings",
        }
    ],
    "priority": "routine",
    "doNotPerform": False,
    "reportedBoolean": True,
    "medicationReference": {"reference": "Medication/med0310"},
    "subject": {
        "reference": "Patient/pat1",
        "display": "Donald Duck",
    },
    "encounter": {
        "reference": "Encounter/f201",
        "display": "encounter who leads to this prescription",
    },
    "supportingInformation": [
        {
            "reference": "Procedure/biopsy",
            "type": "Procedure",
        }
    ],
    "authoredOn": "2015-01-15",
    "requester": {"reference": "Practitioner/f007", "display": "Patrick Pump"},
    "performer": {
        "reference": "Practitioner/f204",
        "display": "Carla Espinosa",
    },
    "performerType": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "26369006",
                "display": "Public Health Nurse",
            }
        ],
        "text": "Nurse",
    },
    "recorder": {
        "reference": "Practitioner/ef81ZrgFqs7ufzYI2X9ixcA3",
        "display": "Epic User",
    },
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "50820005",
                    "display": "Cytopenia (finding)",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-9-cm",
                    "code": "289.9",
                    "display": "Unspecified diseases of blood and blood-forming organs",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-10-cm",
                    "code": "D75.9",
                    "display": "Disease of blood and blood-forming organs, unspecified",
                },
            ],
            "text": "Cytopenia",
        },
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "370388006",
                    "display": "Patient immunocompromised (finding)",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-9-cm",
                    "code": "279.9",
                    "display": "Unspecified disorder of immune mechanism",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-10-cm",
                    "code": "D84.9",
                    "display": "Immunodeficiency, unspecified",
                },
            ],
            "text": "Immunocompromised state",
        },
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "243815002",
                    "display": "Prevention status (finding)",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-9-cm",
                    "code": "V07.8",
                    "display": "Other specified prophylactic or treatment measure",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-10-cm",
                    "code": "Z29.89",
                    "display": "Encounter for other specified prophylactic measures",
                },
            ],
            "text": "Need for pneumocystis prophylaxis",
        },
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "443333004",
                    "display": "Medulloblastoma (disorder)",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-9-cm",
                    "code": "191.6",
                    "display": "Malignant neoplasm of cerebellum NOS",
                },
                {
                    "system": "http://hl7.org/fhir/sid/icd-10-cm",
                    "code": "C71.6",
                    "display": "Malignant neoplasm of cerebellum",
                },
            ],
            "text": "Medulloblastoma",
        },
    ],
    "reasonReference": [
        {
            "reference": "Condition/condition",
        }
    ],
    "instantiatesCanonical": ["canonical"],
    "instantiatesUri": ["uri"],
    "basedOn": [
        {
            "reference": "CarePlan/fM4L7yx-lQwmJcrS7MAT3m1zkSuH8v8LVdM1dkvXzDPc4",
            "type": "CarePlan",
            "display": "BMT Supportive Care Plan",
        },
        {
            "reference": "MedicationRequest/ee02A2FZtICYRsDjH4.zr1tqyCMSVk0A6Uqb--g8q7eQ3",
            "display": "acetaminophen susp 140.8 mg",
        },
    ],
    "courseOfTherapyType": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy",
                "code": "acute",
                "display": "Short course (acute) therapy",
            }
        ],
        "text": "Short course (acute) therapy",
    },
    "insurance": [{"reference": "Coverage/9876B1"}],
    "note": [{"text": "Patient told to take with food"}],
    "dosageInstruction": [
        {
            "sequence": 1,
            "text": "one to two tablets every 4-6 hours as needed for rib pain",
            "additionalInstruction": [
                {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "418914006",
                            "display": "Warning. May cause drowsiness. If affected do not drive or operate machinery. Avoid alcoholic drink (qualifier value)",
                        }
                    ]
                }
            ],
            "patientInstruction": "Take one to two tablets every four to six hours as needed for rib pain",
            "timing": {
                "repeat": {
                    "frequency": 1,
                    "period": 4,
                    "periodMax": 6,
                    "periodUnit": "h",
                }
            },
            "asNeededCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "297217002",
                        "display": "Rib Pain (finding)",
                    }
                ]
            },
            "route": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "26643006",
                        "display": "Oral Route",
                    }
                ]
            },
            "method": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "421521009",
                        "display": "Swallow - dosing instruction imperative (qualifier value)",
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
                                "display": "Ordered",
                            }
                        ]
                    },
                    "doseRange": {
                        "low": {
                            "value": 1,
                            "unit": "TAB",
                            "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
                            "code": "TAB",
                        },
                        "high": {
                            "value": 2,
                            "unit": "TAB",
                            "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
                            "code": "TAB",
                        },
                    },
                }
            ],
        }
    ],
    "dispenseRequest": {
        "validityPeriod": {"start": "2015-01-15", "end": "2016-01-15"},
        "numberOfRepeatsAllowed": 0,
        "quantity": {
            "value": 30,
            "unit": "TAB",
            "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
            "code": "TAB",
        },
        "expectedSupplyDuration": {
            "value": 10,
            "unit": "days",
            "system": "http://unitsofmeasure.org",
            "code": "d",
        },
        "performer": {"reference": "Practitioner/f001"},
    },
    "substitution": {
        "allowedBoolean": True,
        "reason": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-ActReason",
                    "code": "FP",
                    "display": "formulary policy",
                }
            ]
        },
    },
    "detectedIssue": [{"reference": "DetectedIssue/allergy"}],
    "eventHistory": [
        {"reference": "Signature/#signature", "display": "Author's Signature"}
    ],
}
