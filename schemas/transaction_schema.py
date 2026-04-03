from pydantic import BaseModel
from typing import Optional
from datetime import date as DateType

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: DateType
    notes: Optional[str] = None
    user_id: int

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[str] = None
    category: Optional[str] = None
    date: Optional[DateType] = None
    notes: Optional[str] = None