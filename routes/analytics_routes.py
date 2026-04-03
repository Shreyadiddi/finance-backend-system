from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from services.transaction_service import get_summary_service
from fastapi import Query
from utils.helpers import check_user_role

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/analytics/summary")
def get_summary(
    user_id: int = Query(...),
    db: Session = Depends(get_db)
):
    
    check_user_role(db, user_id, ["admin", "analyst"])

    return get_summary_service(db)