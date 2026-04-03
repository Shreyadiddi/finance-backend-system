from sqlalchemy import Column, Integer, Float, String, Date
from database.connection import Base
from sqlalchemy import ForeignKey

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False) # income or expense
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))