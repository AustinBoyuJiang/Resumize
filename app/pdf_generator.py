import requests
import json

# Set your Docmosis Cloud service region URL here
DWSrenderURL = 'https://us1.dws4.docmosis.com/api/render'  # Example for the US region

# Replace 'XXX' with your actual access key
accessKey = 'ZDI3NjY2NmMtMTQzOS00MDg3LWI1NWItNThjM2ViYWRhN2YzOjA3NTU5MDM5ODk'

# Replace 'dataStr' with the data you want to populate in your resume template
dataStr = {
  "first-name": "Austin",
  "last-name": "Jiang",
  "professional-title": "Junior Software Engineer",
  "location": "West Vancouver, BC, Canada",
  "number": "+1 6047541808",
  "email": "austinjiangboyu@gmail.com",
  "objective": "value7",
  "experience1-company": "value8",
  "experience1-title": "value9",
  "experience1-time": "value10",
  "experience1-pt1": "value11",
  "experience1-pt2": "value12",
  "experience1-pt3": "value13",
  "experience1-pt4": "value14",
  "experience2-company": "value15",
  "experience2-title": "value16",
  "experience2-time": "value17",
  "experience2-pt1": "value18",
  "experience2-pt2": "value19",
  "experience2-pt3": "value20",
  "experience2-pt4": "value21",
  "highest-degree-school": "value22",
  "highest-degree": "value23",
  "highest-degree-time": "value24",
  "highest-degree-major": "value25",
  "first-degree-school": "value26",
  "first-degree": "value27",
  "first-degree-time": "value28",
  "first-degree-major": "value29",
  "skill1": "value30",
  "skill2": "value31",
  "skill3": "value32",
  "skill4": "value33"
}

payload = {
    "accessKey": accessKey,
    "templateName": "resume templates/resume template 1.docx",
    "outputName": "MyCustomizedResume.pdf",
    "data": dataStr
}

headers = {'Content-Type': 'application/json'}

response = requests.post(DWSrenderURL, data=str(payload), headers=headers)

if response.status_code == requests.codes.ok:
    with open('MyCustomizedResume.pdf', 'wb') as fd:
        for chunk in response.iter_content(4096):
            fd.write(chunk)
    print("Resume saved as MyCustomizedResume.pdf")
else:
    print("Failed to generate resume")
    print(response.text)
