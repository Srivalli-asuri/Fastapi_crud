from pydantic import BaseModel
from typing import List, Optional

# class StudentBase(BaseModel):
#     name: str
#     roll_no: int

class StudentBase(BaseModel):
    name: str
    email: str
    roll_no: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True


class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class Config:
        orm_mode = True



class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    grade: float

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    id: int
    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    name: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    class Config:
        orm_mode = True
