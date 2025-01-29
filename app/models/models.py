# coding: utf-8
from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    Hashpassword = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    role = Column(Enum('user', 'technician', 'admin'), nullable=False)
    phone_number = Column(String(15), nullable=False)
