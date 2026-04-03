from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from schemas.user_schema import UserCreate
from services.user_service import create_user_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)