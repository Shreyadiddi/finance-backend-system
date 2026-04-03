from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from schemas.transaction_schema import TransactionCreate
from services.transaction_service import(
    create_transaction_service,
    get_all_transaction_service,
    update_transaction_service,
    delete_transaction_service
) 
from typing import Optional
from datetime import date
from utils.helpers import check_user_role
from fastapi import Query
from schemas.transaction_schema import TransactionUpdate

router = APIRouter()

#DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions")
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    check_user_role(db, transaction.user_id, ["admin"])
    
    return create_transaction_service(transaction, db)

@router.get("/transactions")
def get_transactions(
    user_id: int = Query(...),
    type: Optional[str] = None,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    check_user_role(db, user_id, ["admin", "analyst", "viewer"])

    return get_all_transaction_service(
        db, type, category, start_date, end_date
    )

@router.put("/transactions/{transaction_id}")
def update_transaction(
    transaction_id: int,
    updated_data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    return update_transaction_service(transaction_id, updated_data, db)

@router.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    return delete_transaction_service(transaction_id, db)