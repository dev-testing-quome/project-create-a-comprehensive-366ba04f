```python
import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import UUID
import pytz

Base = declarative_base()

class User(Base):
    """Represents a user in the system."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    is_doctor = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now(pytz.utc))
    updated_at = Column(DateTime, default=datetime.datetime.now(pytz.utc), onupdate=datetime.datetime.now(pytz.utc))

    appointments = relationship("Appointment", back_populates="patient")
    prescriptions = relationship("Prescription", back_populates="patient")
    messages_sent = relationship("Message", back_populates="sender", foreign_keys="Message.sender_id")
    messages_received = relationship("Message", back_populates="recipient", foreign_keys="Message.recipient_id")

    def __repr__(self):
        return f'<User {self.username}>'

class Appointment(Base):
    """Represents a scheduled appointment."""
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now(pytz.utc))
    updated_at = Column(DateTime, default=datetime.datetime.now(pytz.utc), onupdate=datetime.datetime.now(pytz.utc))

    patient = relationship("User", back_populates="appointments", foreign_keys=[patient_id])
    doctor = relationship("User", back_populates="appointments", foreign_keys=[doctor_id])

    def __repr__(self):
        return f'<Appointment id={self.id}>'

class Prescription(Base):
    """Represents a patient's prescription."""
    __tablename__ = 'prescriptions'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    medication = Column(String)
    dosage = Column(String)
    instructions = Column(Text)
    refills_remaining = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now(pytz.utc))
    updated_at = Column(DateTime, default=datetime.datetime.now(pytz.utc), onupdate=datetime.datetime.now(pytz.utc))

    patient = relationship("User", back_populates="prescriptions")

    def __repr__(self):
        return f'<Prescription id={self.id}>'

class Message(Base):
    """Represents a message between users."""
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    recipient_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now(pytz.utc))
    updated_at = Column(DateTime, default=datetime.datetime.now(pytz.utc), onupdate=datetime.datetime.now(pytz.utc))

    sender = relationship("User", back_populates="messages_sent", foreign_keys=[sender_id])
    recipient = relationship("User", back_populates="messages_received", foreign_keys=[recipient_id])

    def __repr__(self):
        return f'<Message id={self.id}>'
```