from sqlalchemy.orm import Session
# from .import models,schemas
import models
import schemas


# #create
# def create_user_stud(db:Session,user:schemas.StudentCreate):
#     db_user=models.Student(name=user.name,email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def create_user_stud(db: Session, user: schemas.StudentCreate):
    db_user = models.Student(
        name=user.name,
        email=user.email,
        roll_no=user.roll_no
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#read only one use
def get_user(db:Session,user_id:int):
    return db.query(models.Student).filter(models.Student.id==user_id).first()

#read all users
def get_users(db:Session):
    return db.query(models.Student).all()

#update

def update_user(db:Session,user_id:int,user:schemas.StudentCreate):
    db_user=db.query(models.Student).filter(models.Student.id==user_id).first()
    if db_user:
        db_user.name=user.name
        db_user.email=user.email
        db.commit()
        db.refresh(db_user)
    return db_user

#delete

def delete_user(db:Session,user_id:int):
    db_user=db.query(models.Student).filter(models.Student.id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user