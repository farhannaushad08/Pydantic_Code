from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

#pydantic model/class represent the ideal schema of the data
#field is used to set the range or condition to the numerical value or string based data type 
#annotated is used to add meta data i.e decription , title and contraints using (field function)
#optional is used when there is no necessity to add the paticular info i.e allergies in this code
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

#fuction to print the data
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

#input 
patient_info = {'name':'Farhan', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '22', 'weight': 65.2,'contact_details':{'phone':'2353462'}}

#object of the pydantic class
patient1 = Patient(**patient_info)

#call the call fuction to print
update_patient_data(patient1)
