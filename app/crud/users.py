from sqlalchemy.orm import Session
from fastapi import Depends

from app.api.deps import get_db
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate

def get_users(db: Session):
    return db.query(User).all()

def get_user( db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    return user

def create_user(db: Session, payload: UserCreate):
    user = User(**payload.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(
    db: Session,
    user_id: int, 
    payload: UserUpdate, 
):
    user = get_user(db, user_id)
    if not user:
        return None
    
    data = payload.model_dump(exclude_unset=True)
        
    for field, value in data.items():
        setattr(user, field, value.value if hasattr(value, "value") else value)

    db.commit()
    db.refresh(user)
    return user