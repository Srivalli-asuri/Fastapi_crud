from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..import crud,schemas
from ..db import get_db

router=APIRouter(prefix="/students",tags=["students"])

@router.post("/",response_model=schemas.Student)
def create_student(student:schemas.StudentCreate,db:Session=Depends(get_db)):
    return crud.create_user_stud(db=db,user=student)

@router.get("/",response_model=list[schemas.Student])
def read_students(db:Session=Depends(get_db)):
    return crud.get_users(db=db)


@router.get("/{stu_id}",response_model=schemas.Student)
def read_srudent(user_id:int,db:Session=Depends(get_db)):
    db_stu=crud.get_user(db=db,user_id=user_id)
    if db_stu is None:
        raise HTTPException(status_code=404,detail="Users not found")
    return db_stu

@router.put("/{stu_id}",response_model=schemas.Student)
def update_student(user_id:int,db:Session=Depends(get_db)):
    db_stu=crud.update_user(db=db,user_id=user_id)
    if not db_stu:
        raise HTTPException(status_code=404,detail="Users not found")
    return db_stu

@router.delete("/{user_id}")
def delete_student(user_id:int,db:Session=Depends(get_db)):
    deleted_user=crud.delete_user(db=db,user_id=user_id)
    if not deleted_user:
        return HTTPException(status_code=404,detail="user not found")
    return {"message":|"user deleted succesfully"}