```python
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    """Represents data for creating a new user."""
    username: str = Field(..., min_length=3, max_length=50)
    hashed_password: str = Field(..., min_length=8)  #Consider more robust password validation
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    is_doctor: Optional[bool] = False

class UserUpdate(BaseModel):
    """Represents data for updating an existing user."""
    first_name: Optional[str] = Field(min_length=1, max_length=50)
    last_name: Optional[str] = Field(min_length=1, max_length=50)

class User(BaseModel):
    """Represents a user in the system."""
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
    """Represents data for creating a new appointment."""
    patient_id: int
    doctor_id: int
    date: datetime
    description: Optional[str] = Field(max_length=255)

class Appointment(BaseModel):
    """Represents an appointment in the system."""
    id: int
    patient_id: int
    doctor_id: int
    date: datetime
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PrescriptionCreate(BaseModel):
    """Represents data for creating a new prescription."""
    patient_id: int
    medication: str = Field(..., min_length=1, max_length=100)
    dosage: str = Field(..., min_length=1, max_length=50)
    instructions: str = Field(..., max_length=255)
    refills_left: int = Field(..., ge=0)

class Prescription(BaseModel):
    """Represents a prescription in the system."""
    id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    refills_left: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    """Represents data for creating a new message."""
    sender_id: int
    recipient_id: int
    content: str = Field(..., min_length=1, max_length=1000) #Consider a more generous max length

class Message(BaseModel):
    """Represents a message in the system."""
    id: int
    sender_id: int
    recipient_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
```