RESOURCE = {
    "resourceType": "Appointment",
    "id": "example",
    "identifier": [
        {
            "system": "http://example.org/sampleappointment-identifier",
            "value": "123",
        }
    ],
    "status": "booked",
    "cancelationReason": {
        "coding": [
            {
                "system": "http://hl7.org/fhir/ValueSet/appointment-cancellation-reason",
                "code": "oth-err",
                "display": "Other: Error",
            },
        ]
    },
    "serviceCategory": [
        {
            "coding": [
                {
                    "system": "http://example.org/service-category",
                    "code": "gp",
                    "display": "General Practice",
                }
            ]
        }
    ],
    "serviceType": [
        {"coding": [{"code": "52", "display": "General Discussion"}]}
    ],
    "specialty": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "394814009",
                    "display": "General practice",
                }
            ]
        }
    ],
    "appointmentType": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0276",
                "code": "FOLLOWUP",
                "display": "A follow up visit from a previous appointment",
            }
        ]
    },
    "reasonCode": [
        {
            "coding": [
                {"system": "http://snomed.info/sct", "code": "413095006"}
            ],
            "text": "Clinical Review",
        }
    ],
    "reasonReference": [
        {"reference": "Condition/example", "display": "Severe burn of left ear"}
    ],
    "priority": 5,
    "description": "Discussion on the results of your recent MRI",
    "supportingInformation": [{"reference": "DiagnosticReport/ultrasound"}],
    "start": "2013-12-10T09:00:00Z",
    "end": "2013-12-10T11:00:00Z",
    "slot": [{"reference": "Slot/example"}],
    "created": "2013-10-10",
    "comment": "Further expand on the results of the MRI and determine the next actions that may be appropriate.",
    "basedOn": [{"reference": "ServiceRequest/myringotomy"}],
    "participant": [
        {
            "actor": {
                "reference": "Patient/example",
                "display": "Peter James Chalmers",
            },
            "required": "required",
            "status": "accepted",
        },
        {
            "type": [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                            "code": "ATND",
                        }
                    ]
                }
            ],
            "actor": {
                "reference": "Practitioner/example",
                "display": "Dr Adam Careful",
            },
            "required": "required",
            "status": "accepted",
        },
        {
            "actor": {
                "reference": "Location/1",
                "display": "South Wing, second floor",
            },
            "required": "required",
            "status": "accepted",
        },
    ],
    "requestedPeriod": [{"start": "2016-06-02", "end": "2016-06-09"}],
}
