RESOURCE = {
    "resourceType": "Specimen",
    "id": "101",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: 101</p><p><b>contained</b>: </p><p><b>identifier</b>: 23234352356</p><p><b>accessionIdentifier</b>: X352356</p><p><b>status</b>: available</p><p><b>type</b>: Venous blood specimen <span>(Details : {SNOMED CT code '122555007' = 'Venous blood specimen', given as 'Venous blood specimen'})</span></p><p><b>subject</b>: <a>Peter Patient</a></p><p><b>receivedTime</b>: 04/03/2011 7:03:00 AM</p><p><b>request</b>: <a>ServiceRequest/example</a></p><h3>Collections</h3><table><tr><td>-</td><td><b>Collector</b></td><td><b>Collected[x]</b></td><td><b>Quantity</b></td><td><b>Method</b></td><td><b>BodySite</b></td></tr><tr><td>*</td><td><a>Practitioner/example</a></td><td>30/05/2011 6:15:00 AM</td><td>6 mL</td><td>Line, Venous <span>(Details : {http://terminology.hl7.org/CodeSystem/v2-0488 code 'LNV' = 'Line, Venous)</span></td><td>Right median cubital vein <span>(Details : {SNOMED CT code '49852007' = 'Median cubital vein', given as 'Structure of median cubital vein (body structure)'})</span></td></tr></table><h3>Containers</h3><table><tr><td>-</td><td><b>Identifier</b></td><td><b>Description</b></td><td><b>Type</b></td><td><b>Capacity</b></td><td><b>SpecimenQuantity</b></td><td><b>Additive[x]</b></td></tr><tr><td>*</td><td>48736-15394-75465</td><td>Green Gel tube</td><td>Vacutainer <span>(Details )</span></td><td>10 mL</td><td>6 mL</td><td>id: hep; Lithium/Li Heparin <span>(Details : {http://terminology.hl7.org/CodeSystem/v3-EntityCode code 'HEPL' = 'Lithium/Li Heparin)</span></td></tr></table><p><b>note</b>: Specimen is grossly lipemic</p></div>",
    },
    "contained": [
        {
            "resourceType": "Substance",
            "id": "hep",
            "code": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v3-EntityCode",
                        "code": "HEPL",
                    }
                ]
            },
        }
    ],
    "identifier": [
        {
            "system": "http://ehr.acme.org/identifiers/collections",
            "value": "23234352356",
        }
    ],
    "accessionIdentifier": {
        "system": "http://lab.acme.org/specimens/2011",
        "value": "X352356",
    },
    "status": "available",
    "type": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "122555007",
                "display": "Venous blood specimen",
            }
        ],
        "text": "venous blood",
    },
    "subject": {
        "reference": "Patient/example",
        "display": "Peter Patient",
        "type": "Patient",
    },
    "receivedTime": "2011-03-04T07:03:00Z",
    "request": [{"reference": "ServiceRequest/example"}],
    "collection": {
        "collector": {"reference": "Practitioner/example"},
        "collectedDateTime": "2011-05-30T06:15:00Z",
        "quantity": {"value": 6, "unit": "mL"},
        "method": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v2-0488",
                    "code": "LNV",
                }
            ],
            "text": "Venous Line",
        },
        "bodySite": {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "49852007",
                    "display": "Structure of median cubital vein (body structure)",
                }
            ],
            "text": "Right median cubital vein",
        },
        "fastingStatusCodeableConcept": {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "123",
                    "display": "yes",
                }
            ],
            "text": "fasting since midnight",
        },
        "fastingStatusDuration": {
            "value": "3",
            "unit": "days",
            "system": "ucum.org",
            "code": "3d",
        },
    },
    "processing": [
        {
            "description": "Acidify to pH < 3.0 with 6 N HCl.",
            "procedure": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0373",
                        "code": "ACID",
                    }
                ]
            },
            "additive": [{"display": "6 N HCl"}],
            "timeDateTime": "2015-08-18T08:10:00Z",
        }
    ],
    "container": [
        {
            "identifier": [{"value": "48736-15394-75465"}],
            "description": "Green Gel tube",
            "type": {"text": "Vacutainer"},
            "capacity": {"value": 10, "unit": "mL"},
            "specimenQuantity": {"value": 6, "unit": "mL"},
            "additiveReference": {"reference": "#hep"},
        }
    ],
    "condition": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "abc1",
                    "display": "bad heart",
                }
            ],
            "text": "example_condition",
        },
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "abc3",
                    "display": "worse heart",
                }
            ],
            "text": "example_condition_2",
        },
    ],
    "parent": [
        {"reference": "Specimen/example1", "display": "Whole Blood"},
    ],
    "note": [
        {
            "text": "Specimen is grossly lipemic",
            "authorString": "Doctor Judy",
            "time": "2011-03-01T07:03:00Z",
        }
    ],
}
