# we want to check in the Email if their is @hdfc.com and @icici.com in the email address and if not then we want to raise an error and also we want to check if the name is not empty and also we want to check if the age is greater than 0 and also we want to check if the weight is greater than 0 .
# 
# 
# Field validator works only on single parameter for but if we want to validate multiple parameters then we can use Model validator.



from pydantic  import BaseModel ,EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict  , Optional  , Annotated

class Patient(BaseModel):

    name: str
    Email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_info: Dict[str, str]

    @field_validator('Email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Email domain must be either hdfc.com or icici.com')
        return value    
    

    @field_validator('name' , mode = 'after')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
 


    @field_validator('age' ,mode= 'after')
    @classmethod
    def age_validator(cls, value):
        if value <= 0:
            raise ValueError('Age must be a positive integer')
        return value



    @field_validator('weight' ,mode= 'after')
    @classmethod
    def weight_validator(cls, value):
        if value <= 0:
            raise ValueError('Weight must be a positive number')
        return value


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

patient_info = {'name': 'John Doe', 'Email': 'john.doe@hdfc.com', 'age': 30, 'weight': 70.5, 'married': True, 'allergies': ['peanuts'], 'contact_info': { 'phone': '123-456-7890'}}

Patient1 = Patient(**patient_info )

update_patient_date(Patient1)