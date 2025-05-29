RESOURCE = {
    "resourceType": "Location",
    "id": "3ad0687e-f477-468c-afd5-fcc2bf897819",
    "identifier": [
        {
            "use": "usual",
            "type": {"text": "NPI"},
            "system": "http://hl7.org/fhir/sid/us-npi",
            "value": "1215921457",
        },
        {
            "use": "usual",
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.686980",
            "value": "84275011",
        },
    ],
    "status": "active",
    "operationalStatus": {
        "system": "http://terminology.hl7.org/CodeSystem/v2-0116",
        "code": "H",
        "display": "Housekeeping",
    },
    "name": "KOP Nutrition",
    "alias": ["KNU"],
    "description": "Second floor of the Old South Wing, formerly in use by Psychiatry",
    "type": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
                    "code": "RNEU",
                    "display": "Neuroradiology unit",
                }
            ]
        }
    ],
    "mode": "instance",
    "telecom": [
        {"system": "phone", "value": "215-590-5223", "rank": 1},
        {"system": "fax", "value": "215-590-4460"},
    ],
    "address": {
        "line": ["550 South Goddard Blvd"],
        "city": "King of Prussia",
        "state": "Pennsylvania",
        "postalCode": "19406",
        "country": "United States",
    },
    "physicalType": {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/location-physical-type",
                "code": "wi",
                "display": "Wing",
            }
        ]
    },
    "managingOrganization": {
        "reference": "Organization/organization",
        "display": "Organization",
    },
    "partOf": {"reference": "Location/location", "display": "Location"},
    "hoursOfOperation": {"allDay": True},
    "endpoint": [{"reference": "Endpoint/endpoint"}],
}
