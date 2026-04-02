from turtle import title

from pydantic  import BaseModel ,EmailStr , AnyUrl , Field
from typing import List , Dict  , Optional ,Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(..., min_length=50,title = "Name of the patient", description="Name must be a non-empty string")]
    Email: EmailStr
    linkdinUrl: AnyUrl
    age: int
    weight: float = Field(..., gt=0, description="Weight must be greater than zero")
    married: Annotated[bool, Field(..., description="Marital status of the patient")]
    allergies: Optional[List[str]] = None 
    contact_info: Dict[str, str]



def insert_patient_date(patient: Patient):

    print(patient.name)
    print(patient.age)
    
    print('Patient data inserted successfully')


def update_patient_date(patient: Patient):

    print(patient.name)
    print(patient.age)
    
    print('Patient data updated successfully')

pateint_info = {'name': 'John Doe', 'Email': 'abc@gmail.com','linkdinUrl': 'https://www.linkedin.com/in/johndoe', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['peanuts'], 'contact_info': {'phone': '123-456-7890'}}

pateint_info['name'] = 'Johnathan Alexander Doe, a patient with a very long name for testing.'
Patient1 = Patient(**pateint_info )

update_patient_date(Patient1)
