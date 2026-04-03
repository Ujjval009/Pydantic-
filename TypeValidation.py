from pydantic  import BaseModel
from typing import List , Dict  , Optional 

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_info: Dict[str, str]

def insert_patient_date(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)        
    print(patient.contact_info)
    print('Patient data inserted successfully')


def update_patient_date(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info) 
    print('Patient data updated successfully')

pateint_info = {'name': 'John Doe', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['peanuts'], 'contact_info': {'email': 'john.doe@example.com', 'phone': '123-456-7890'}}

Patient1 = Patient(**pateint_info )

update_patient_date(Patient1)