RESOURCE = {
    "resourceType": "BodyStructure",
    "id": "tumor",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: tumor</p><p><b>identifier</b>: 12345</p><p><b>morphology</b>: Splenic mass <span>(Details : {SNOMED CT code '4147007' = 'Mass', given as 'Mass (morphologic abnormality)'})</span></p><p><b>location</b>: Spleen <span>(Details : {SNOMED CT code '78961009' = 'Spleen', given as 'Splenic structure (body structure)'})</span></p><p><b>description</b>: 7 cm maximum diameter</p><p><b>image</b>: </p><p><b>patient</b>: <a>Patient/example</a></p></div>",
    },
    "active": True,
    "identifier": [
        {
            "system": "http://goodhealth.org/bodystructure/identifiers",
            "value": "12345",
        }
    ],
    "morphology": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "4147007",
                "display": "Mass (morphologic abnormality)",
            }
        ],
        "text": "Splenic mass",
    },
    "location": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "78961009",
                "display": "Splenic structure (body structure)",
            }
        ],
        "text": "Spleen",
    },
    "locationQualifier": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "419161000",
                    "display": "Unilateral left",
                }
            ],
            "text": "Left",
        },
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "263929005",
                    "display": "Volar",
                }
            ],
            "text": "Volar",
        },
    ],
    "description": "7 cm maximum diameter",
    "image": [
        {
            "contentType": "application/dicom",
            "url": "http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details",
        }
    ],
    "patient": {"reference": "Patient/example"},
}
