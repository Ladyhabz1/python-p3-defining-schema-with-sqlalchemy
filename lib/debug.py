#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_sandbox import Student, Base

engine = create_engine('sqlite:///students.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()  # Debugger will pause here

    # Example: Add a student to the database
    new_student = Student(name="Habiba")
    session.add(new_student)
    session.commit()

    # Fetch all students to verify
    students = session.query(Student).all()
    print(students)
