#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # Define table name

    id = Column(Integer, primary_key=True)  # Primary Key
    name = Column(String)  # Example column

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')  # Create database
    Base.metadata.create_all(engine)  # Create tables
