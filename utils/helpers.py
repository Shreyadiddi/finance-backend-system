from fastapi import HTTPException
from models.user import User

def check_user_role(db, user_id, allowed_roles):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, details="User not found")
    
    if user.role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Access denied")
    
    return user