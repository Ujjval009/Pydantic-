 #Field validator works only on single parameter for but if we want to validate multiple parameters then we can use Model validator.

from pydantic  import BaseModel ,EmailStr , AnyUrl , Field , field_validator, model_validator
from typing import List , Dict  , Optional  , Annotated

class Patient(BaseModel):

    name: str
    Email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_info: Dict[str, str]

    
    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency_contact' not in model.contact_info:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model


    


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



patient_info = {'name': 'John Doe', 'Email': 'john.doe@hdfc.com', 'age': 90, 'weight': 70.5, 'married': True, 'allergies': ['peanuts'], 'contact_info': { 'emergency_contact': '164346548', 'phone': '123-456-7890'}}




Patient1 = Patient(**patient_info )



update_patient_date(Patient1) 