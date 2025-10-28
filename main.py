from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
from db import engine,get_db


# Create all tables in the database on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Grade Management System")

# CREATE student
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_user_stud(db=db, user=student)

# READ all students
@app.get("/students/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

# READ single student
@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_user(db=db, user_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# UPDATE student
@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_user(db=db, user_id=student_id, user=student)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

# DELETE student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_user(db=db, user_id=student_id)
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
