RESOURCE = {
    "resourceType": "Consent",
    "id": "consent-example-basic",
    "text": {
        "status": "generated",
        "div": '<div xmlns="http://www.w3.org/1999/xhtml">\n\t\t\t<p>\n\tAuthorize Normal access for Treatment\n\t\t\t</p>\n\t\t\t<p>\n    Patient &quot;P. van de Heuvel&quot; wishes to have all of the PHI collected at the Good Health Psychiatric Hospital \n   available for normal treatment use.\n\t\t\t</p>\n\t\t</div>',
    },
    "identifier": [
        {
            "system": "urn:oid:2.16.840.1.113883.3.72.5.9.1",
            "value": "494e0c7a-a69e-4fb4-9d02-6aae747790d7",
        }
    ],
    "status": "active",
    "scope": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/consentscope",
                "code": "patient-privacy",
            }
        ]
    },
    "category": [
        {"coding": [{"system": "http://loinc.org", "code": "59284-0"}]}
    ],
    "patient": {"reference": "Patient/f001", "display": "P. van de Heuvel"},
    "dateTime": "2016-05-11",
    "performer": [{"reference": "Patient/72"}],
    "organization": [{"reference": "Organization/f001"}],
    "sourceAttachment": {"title": "The terms of the consent in lawyer speak."},
    "policy": [{"uri": "urn:uuid:53fefa32-fcbb-4ff8-8a92-55ee120877b7"}],
    "policyRule": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": "OPTIN",
            }
        ]
    },
    "verification": [{"verified": True, "verificationDate": "2015-10-10"}],
    "provision": {
        "period": {"start": "2015-10-10", "end": "2016-10-10"},
        "actor": [
            {
                "role": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                            "code": "PRCP",
                        }
                    ]
                },
                "reference": {"reference": "Practitioner/13"},
            }
        ],
        "action": [
            {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/consentaction",
                        "code": "access",
                    }
                ]
            }
        ],
        "securityLabel": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/v3-Confidentiality",
                "code": "N",
            }
        ],
        "purpose": [
            {
                "system": "http://terminology.hl7.org/ValueSet/v3-PurposeOfUse",
                "code": "PurposeOfUse",
                "display": "purpose of use",
            }
        ],
        "class": [
            {
                "system": "http://hl7.org/fhir/ValueSet/consent-content-class",
                "code": "urn:ihe:pcc:xphr:2007",
                "display": "Personal Health Records. Also known as HL7 CCD and HITSP C32",
            }
        ],
        "code": [
            {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/ValueSet/consent-content-code",
                        "code": "1-8",
                        "display": "Acyclovir [Susceptibility]",
                    }
                ]
            }
        ],
        "data": [
            {
                "meaning": "authoredby",
                "reference": {
                    "reference": "DocumentReference/documentreference"
                },
            }
        ],
        "provision": [
            {
                "type": "permit",
                "actor": [
                    {
                        "role": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                                    "code": "AUT",
                                }
                            ]
                        },
                        "reference": {"reference": "Practitioner/xcda-author"},
                    }
                ],
                "class": [
                    {
                        "system": "urn:ietf:bcp:13",
                        "code": "application/hl7-cda+xml",
                    }
                ],
                "code": [
                    {
                        "coding": [
                            {"system": "http://loinc.org", "code": "34133-9"}
                        ]
                    },
                    {
                        "coding": [
                            {"system": "http://loinc.org", "code": "18842-5"}
                        ]
                    },
                ],
            }
        ],
    },
}
