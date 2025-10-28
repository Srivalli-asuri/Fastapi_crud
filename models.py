from sqlalchemy import Column,Integer,String
# from .db import Base
from db import Base


# class Student(Base):
#     __tablename__="students"

#     id=Column(Integer,primary_key=True,index=True)
#     name=Column(String(50))

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100))
    roll_no = Column(Integer)

class Subject(Base):
    __tablename__="Subjects"

    no=Column(Integer,primary_key=True)
    sub=Column(String(10))

class Grade(Base):
    __tablename__="Grades"

    marks=Column(Integer,primary_key=True)
    grade=Column(String(10))

class Teacher(Base):
    __tablename__="Teachers"

    id=Column(Integer,primary_key=True)
    name=Column(String(10))
