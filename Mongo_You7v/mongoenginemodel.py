
from mongoengine import Document,StringField,EmailField,IntField

class User(Document):
    email=EmailField(required=True)
    first_name = StringField(max_length=255)
    last_name = StringField(max_length=255)
    age=IntField(max_length=255)

    # {
    #     email:"mak@gmail.com",
    #     first_name:"Mahabub",
    #     last_name:"Rahman",
    #     age:25
    # }