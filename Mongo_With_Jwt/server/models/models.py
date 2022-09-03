from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class DbReceipt(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    receipt_id: int = Field(...)
    email: EmailStr = Field(...)
    create_at: datetime = datetime.now()
    token_status: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }






CATEGORIES = (
    ('REGISTRATION', 'registration'),
    ('ADMIN', 'admin'),
    ('XRAY', 'xray'),
    ('MDOCTOR', 'mdoctor'),
    ('EYE', 'eye'),
    ('FDOCTOR', 'fdoctor'),
    ('URIN', 'urin')
)
RECEIPT_STATUSES = (
    ('PROCESSING', 'processing'),
    ('INTRANSIT', 'intransit'),
    ('HOLD', 'hold'),
    ('DELIVERED', 'delivered')
)