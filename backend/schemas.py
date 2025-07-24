from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    first_name: str
    last_name: str
    is_doctor: Optional[bool] = False

class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_doctor: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date: datetime
    description: str

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: datetime
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PrescriptionCreate(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    refills_remaining: int

class Prescription(BaseModel):
    id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    refills_remaining: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class Message(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
