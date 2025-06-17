# def inser_patient_detail(name: str, age: int):
#      if type(name) == str and type(age) == int:
#          print(name)
#          print(age)
#          print("inserted in db.")
         
#      else:
#          raise TypeError('datatype mismatch')

from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    
patient_info = {'name': 'Ashu','age':30, 'weight': 70, 'allergies': ['dust', 'pollen'], 'contact_details':{'email':'abc@gmail.com', 'phone':'6584232178'}}

patient1 = Patient(**patient_info)

def insert_patient_detail(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted in db.")
    
insert_patient_detail(patient1)