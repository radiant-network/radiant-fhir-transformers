RESOURCE = {
  "resourceType": "ServiceRequest",
  "id": "di_abcd_efg",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: di</p><p><b>status</b>: active</p><p><b>intent</b>: original-order</p><p><b>code</b>: Chest CT <span>(Details : {LOINC code '24627-2' = 'Chest CT)</span></p><p><b>subject</b>: <a>Patient/dicom</a></p><p><b>occurrence</b>: 08/05/2013 9:33:27 AM</p><p><b>requester</b>: <a>Dr. Adam Careful</a></p><p><b>reasonCode</b>: Check for metastatic disease <span>(Details )</span></p></div>"
  },
  "status": "active",
  "intent": "original-order",
  "priority": "routine",
  "basedOn": [
    {
      "display": "ServiceRequest for Myringotomy and insertion of tympanic ventilation tube",
      "reference": "somereferencestring"
    }
  ],
  "code": {
    "coding": [
      {
        "system": "http://loinc.org",
        "code": "24627-2"
      }
    ],
    "text": "Chest CT"
  },
  "quantityQuantity": {
    "value":"5",
    "comparator":"something",
    "unit":"acres",
    "system":"imperial_units",
    "code":"konami",
  },
  "quantityRatio":{
      "numerator":{
          "value": 1, #change this back to numeric.  Only switched to string so validation will pass 
          "comparator":5,
          "unit":"gallons",
          "system":"metric",
          "code":"gl",
      },
      "denominator":{
          "value": 2,
          "comparator":5,
          "unit":"gallons",
          "system":"metric",
          "code":"gl",
      }
  },
  "quantityRange":{
      "low":{
          "value":1,
          "unit":"part",
      },
      "high":{
          "value":10,
          "unit":"part",
      },      
  },
  "doNotPerform": True,
  "subject": {
    "reference": "Patient/dicom.example.pt",
    "display": "Judy Test"
  },
  "encounter": {
    "reference": "Encounter/example",
    "display": "1234encounter"
  },
  "occurrenceDateTime": "2013-05-08T09:33:27+07:00",
  "occurrencePeriod": {
      "start":"2013-05-08",
      "end":"2013-05-09",
  },
  "occurrenceTiming": {
    "repeat": {
      "count": 20,
      "countMax": 30,
      "frequency": 3,
      "period": 1,
      "periodUnit": "wk"
    },
  },
  "requester": {
    "reference": "Practitioner/example.doc",
    "display": "Dr. Adam Careful"
  },
  "asNeededBoolean": False,
  "asNeededCodeableConcept": {
      "coding":[
        {
          "system": "http://mysystem.org",
          "code": "123-yes",
        },
      ],
      "text": "as needed text example"
  },
  "authoredOn": "2014-02-14",
  "reasonCode": [
    {
      "text": "Check for metastatic disease"
    }
  ],
  "performerType": {
    "coding": [
      {
        "system": "http://orionhealth.com/fhir/apps/specialties",
        "code": "ent",
        "display": "ENT"
      }
    ],
    "text":"Ear Nose and Throat"
  },
  "bodySite": [
    {
      "coding": [
        {
          "display": "Right arm"
        }
      ],
      "text": "Right arm"
    }
  ],
  "patientInstruction": "Start with 30kg 10-15 repetitions for three sets and increase in increments of 5kg when you feel ready",
  "note": [
    {
      "text": "patient is afraid of needles"
    }
  ],
}