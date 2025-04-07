"""
Test helper class for FHIR resource type Patient
"""

from tests.data.base import FhirResourceTestHelper

RESOURCE = {
    "resourceType": "Patient",
    "id": "eNuTIJvJoX5g5enjtR.Ul4ASEfAlFvJjiahhGyW1xd8x43",
    "extension": [
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.698084.130.657370.8551999258",
                        "code": "Female",
                        "display": "Female",
                    }
                ]
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/legal-sex",
        },
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "urn:oid:1.2.840.114350.1.13.20.3.7.10.698084.130.657370.8551999258",
                        "code": "Female",
                        "display": "Female",
                    }
                ]
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/sex-for-clinical-use",
        },
        {
            "extension": [
                {
                    "valueCoding": {
                        "system": "urn:oid:2.16.840.1.113883.6.238",
                        "code": "2106-3",
                        "display": "White",
                    },
                    "url": "ombCategory",
                },
                {"valueString": "White", "url": "text"},
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
        },
        {
            "extension": [
                {
                    "valueCoding": {
                        "system": "urn:oid:2.16.840.1.113883.6.238",
                        "code": "2186-5",
                        "display": "Not Hispanic or Latino",
                    },
                    "url": "ombCategory",
                },
                {"valueString": "Not Hispanic or Latino", "url": "text"},
            ],
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
        },
        {
            "valueCode": "248152002",
            "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-sex",
        },
        {
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "LA29519-8",
                        "display": "she/her/her/hers/herself",
                    }
                ]
            },
            "url": "http://open.epic.com/FHIR/StructureDefinition/extension/calculated-pronouns-to-use-for-text",
        },
    ],
    "identifier": [
        {
            "use": "usual",
            "type": {"text": "CEID"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.3.688884.100",
            "value": "CP2X5WT625RHKPL",
        },
        {
            "use": "usual",
            "type": {"text": "EPI"},
            "system": "urn:oid:2.16.840.7.740741.2",
            "value": "82000393",
        },
        {
            "use": "usual",
            "type": {"text": "EXTERNAL"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698084",
            "value": "Z8200393",
        },
        {
            "use": "usual",
            "type": {"text": "FHIR"},
            "system": "http://open.epic.com/FHIR/StructureDefinition/patient-dstu2-fhir-id",
            "value": "Tyw6trYvozNNXODQ6q.0MMd9EIHlpJdOEqC.lHa7jj4cB",
        },
        {
            "use": "usual",
            "type": {"text": "INTERNAL"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.2.698084",
            "value": "  Z8200393",
        },
        {
            "use": "usual",
            "type": {"text": "MYC"},
            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.5.737384.100100",
            "value": "BROOKELUOTESTPROXY",
        },
        {
            "use": "usual",
            "system": "urn:oid:2.16.840.1.113883.4.1",
            "_value": {
                "extension": [
                    {
                        "valueString": "xxx-xx-xxxx",
                        "url": "http://hl7.org/fhir/StructureDefinition/rendered-value",
                    }
                ]
            },
        },
    ],
    "active": True,
    "name": [
        {
            "use": "official",
            "text": "Testing Careeverywhere",
            "family": "Careeverywhere",
            "given": ["Testing"],
        },
        {
            "use": "usual",
            "text": "Testing Careeverywhere",
            "family": "Careeverywhere",
            "given": ["Testing"],
        },
    ],
    "telecom": [
        {"system": "phone", "value": "215-590-1000", "use": "home", "rank": 1},
        {
            "system": "phone",
            "value": "267-760-7648",
            "use": "mobile",
            "rank": 2,
        },
        {"system": "email", "value": "luobt@chop.edu", "rank": 1},
    ],
    "gender": "Female",
    "birthDate": "2005-02-27",
    "deceasedBoolean": False,
    "address": [
        {
            "use": "home",
            "line": ["100 CareEverywhere Lane"],
            "city": "PHILA",
            "district": "Philadelphia",
            "state": "PA",
            "postalCode": "19104",
            "country": "US",
        },
        {
            "use": "old",
            "line": ["100 CareEverywhere Lane"],
            "city": "PHILA",
            "district": "Philadelphia",
            "state": "PA",
            "postalCode": "19104",
            "country": "US",
        },
    ],
    "maritalStatus": {"text": "Single"},
    "contact": [
        {
            "relationship": [
                {
                    "coding": [
                        {
                            "system": "urn:oid:1.2.840.114350.1.13.20.3.7.4.827665.1000",
                            "code": "4",
                            "display": "Mother",
                        }
                    ],
                    "text": "Mother",
                }
            ],
            "name": {"use": "usual", "text": "Careeverywhere, Mom"},
            "telecom": [
                {"system": "phone", "value": "215-590-1000", "use": "home"}
            ],
        }
    ],
    "communication": [
        {
            "language": {
                "coding": [
                    {
                        "system": "urn:ietf:bcp:47",
                        "code": "en",
                        "display": "English",
                    }
                ],
                "text": "English",
            },
            "preferred": True,
        }
    ],
}

EXPECTED_OUTPUT = {
    "given_name": "Testing",
    "family_name": "Careeverywhere",
    "birth_date": "2005-02-27",
    "active": True,
    "gender": "Female",
}


class PatientTestHelper(FhirResourceTestHelper):
    """
    A helper class for testing transformations of the FHIR 'Patient' resource.

    This class extends the FhirResourceTestHelper and is specifically
    designed to assist in testing the transformation of the 'Patient' resource.

    It predefines the resource type as 'Patient'
    and initializes the resource with the specific 'Patient' resource payload
    and its expected transformation output.

    Attributes:
        resource_type (str): The type of FHIR resource being tested, which
          is set to 'Patient'.

        resource (dict): The raw FHIR 'Patient' resource payload to be tested.

        expected_output (dict): The expected transformation result of the
          'Patient' resource payload.
    """

    resource_type = "Patient"

    def __init__(self):
        super().__init__(RESOURCE, EXPECTED_OUTPUT)
