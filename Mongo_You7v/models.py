
from fastapi import Body

from mongoengine import Document,StringField,IntField,ListField
from pydantic import BaseModel
class Employee(Document):
    employee_id=IntField(max_length=11)
    name=StringField(max_length=100)
    age=IntField()
    teams=ListField()

class NewEmployee(BaseModel):
    employee_id:int
    name:str
    age:int=Body(None,gt=18)
    teams:list
    
class User(Document):
    username=StringField(max_length=100)
    password=StringField(max_length=100)

class NewUser(BaseModel):
    username:str
    password:str

        

    