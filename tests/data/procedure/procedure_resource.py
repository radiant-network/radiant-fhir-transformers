RESOURCE = {
    "resourceType": "Procedure",
    "id": "f201",
    "identifier": [
        {
            "use": "usual",
            "type": {"text": "ORD"},
            "system": "urn:oid:1.2.840.114350.1.13.861.1.7.2.798268",
            "value": "3287774",
        },
        {
            "use": "usual",
            "type": {"text": "EAP"},
            "system": "urn:oid:1.2.840.114350.1.13.861.1.7.2.696580",
            "value": "307",
        },
    ],
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated Narrative: Procedure</b><a name="f201"> </a></p><div style="display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%"><p style="margin-bottom: 0px">Resource Procedure &quot;f201&quot; </p></div><p><b>instantiatesCanonical</b>: <a href="http://example.org/fhir/PlanDefinition/KDN5">http://example.org/fhir/PlanDefinition/KDN5</a></p><p><b>status</b>: completed</p><p><b>code</b>: Chemotherapy <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="https://browser.ihtsdotools.org/">SNOMED CT</a>#367336001)</span></p><p><b>subject</b>: <a href="patient-example-f201-roel.html">Patient/f201: Roel</a> &quot;Roel&quot;</p><p><b>encounter</b>: <a href="encounter-example-f202-20130128.html">Encounter/f202: Roel\'s encounter on January 28th, 2013</a></p><p><b>occurrence</b>: 2013-01-28T13:31:00+01:00 --&gt; 2013-01-28T14:27:00+01:00</p><h3>Performers</h3><table class="grid"><tr><td>-</td><td><b>Function</b></td><td><b>Actor</b></td></tr><tr><td>*</td><td>Medical oncologist <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="https://browser.ihtsdotools.org/">SNOMED CT</a>#310512001)</span></td><td><a href="practitioner-example-f201-ab.html">Practitioner/f201: Dokter Bronsig</a> &quot;Dokter Bronsig&quot;</td></tr></table><h3>Reasons</h3><table class="grid"><tr><td>-</td><td><b>Concept</b></td></tr><tr><td>*</td><td>DiagnosticReport/f201 <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> ()</span></td></tr></table><p><b>bodySite</b>: <span title=" TODO Why can\'t this be Resource (any) AND String? ">Sphenoid bone <span style="background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki"> (<a href="https://browser.ihtsdotools.org/">SNOMED CT</a>#272676008)</span></span></p><p><b>note</b>: <span title=" No outcomes, reports, complications or follow-ups were available ">Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding.</span></p></div>',
    },
    "instantiatesCanonical": ["http://example.org/fhir/PlanDefinition/KDN5"],
    "instantiatesUri": ["http://example.org/fhir/PlanDefinition/KDN5"],
    "basedOn": [
        {
            "reference": "ServiceRequest/eD4Zh1drvNSQaox4sq5nvWDnOp6jrCft8Pdwty3sU8a83",
            "display": "Determination of Refractive State",
        }
    ],
    "partOf": [
        {
            "reference": "Procedure/part-of-referenced-event",
            "display": "Part of referenced event",
        }
    ],
    "status": "completed",
    "statusReason": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "182992009",
                "display": "Treatment completed (situation)",
            }
        ],
        "text": "Treatment completed",
    },
    "category": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "103693007",
                "display": "Diagnostic procedure",
            }
        ],
        "text": "Ordered Procedures",
    },
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "367336001",
                "display": "Chemotherapy",
            }
        ]
    },
    "subject": {
        "reference": "Patient/f201",
        "display": "Roel",
    },
    "encounter": {
        "reference": "Encounter/f202",
        "display": "Roel's encounter on January 28th, 2013",
    },
    "performedDate": "2013-01-28T14:27:00+01:00",
    "performedPeriod": {
        "start": "2013-01-28T13:31:00+01:00",
        "end": "2013-01-28T14:27:00+01:00",
    },
    "asserter": {
        "reference": "Practitioner/eOJIO17tsdF3l7OssxPihIg3",
        "type": "Practitioner",
    },
    "performer": [
        {
            "function": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "310512001",
                        "display": "Medical oncologist",
                    }
                ]
            },
            "actor": {
                "reference": "Practitioner/f201",
                "display": "Dokter Bronsig",
            },
        }
    ],
    "reasonCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "400097005",
                    "display": "Ingrowing nail",
                }
            ],
            "text": "Ingrowing nail",
        }
    ],
    "reasonReference": [
        {
            "reference": "Condition/reason",
            "type": "Condition",
            "display": "The justification that the procedure was performed",
        }
    ],
    "bodySite": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "272676008",
                    "display": "Sphenoid bone",
                }
            ]
        }
    ],
    "outcome": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "385669000",
                "display": "Successful",
            }
        ]
    },
    "report": [{"reference": "DiagnosticReport/chemotherapy"}],
    "complication": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "134006",
                    "display": "Decreased hair growth",
                }
            ]
        }
    ],
    "complicationDetail": [{"reference": "Condition/complication"}],
    "followUp": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "183651009",
                    "display": "Chemotherapy follow-up (procedure)",
                }
            ]
        }
    ],
    "note": [
        {
            "text": "Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding."
        }
    ],
    "focalDevice": [
        {
            "action": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "231361000",
                        "display": " Attention to catheter (procedure)",
                    }
                ]
            },
            "manipulated": {"reference": "Device/manipulated"},
        }
    ],
    "usedReference": [{"display": "Colonoscope device"}],
    "usedCode": [
        {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "9017009",
                    "display": "Ventricular intracranial catheter",
                }
            ]
        }
    ],
}
