from models.transaction import Transaction

def create_transaction_service(transaction, db):
    new_transcation = Transaction(
        amount=transaction.amount,
        type=transaction.type,
        category=transaction.category,
        date=transaction.date,
        notes=transaction.notes,
        user_id=transaction.user_id
    )

    db.add(new_transcation)
    db.commit()
    db.refresh(new_transcation)

    return {
        "message": "Transaction added successfully",
        "data": {
            "id": new_transcation.id,
            "amount": new_transcation.amount
        }
    }

def get_all_transaction_service(db, type=None, category=None, start_date=None, end_date=None):
    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)
    
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    
    if end_date:
        query = query.filter(Transaction.date <= end_date)

    return query.all()

from sqlalchemy import func

def get_summary_service(db):
    total_income = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "income").scalar() or 0
    
    total_expense = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "expense").scalar() or 0
    
    balance = total_income - total_expense

    category_data = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).group_by(Transaction.category).all()

    category_summary = [
        {"category": cat, "total": amt}
        for cat, amt in category_data
    ]

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "category_breakdown": category_summary
    }

def update_transaction_service(transaction_id, updated_data, db):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return {"error": "Transaction not found"}
    
    if updated_data.amount is not None:
        transaction.amount = updated_data.amount

    if updated_data.type is not None:
        transaction.type = updated_data.type

    if updated_data.category is not None:
        transaction.category = updated_data.category

    if updated_data.date is not None:
        transaction.date = updated_data.date

    if updated_data.notes is not None:
        transaction.notes = updated_data.notes

    db.commit()
    db.refresh(transaction)

    return {"message": "Trasaction updated successfully"}

def delete_transaction_service(transaction_id, db):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        return {"error": "Transaction not found"}
    
    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted successfuly"}