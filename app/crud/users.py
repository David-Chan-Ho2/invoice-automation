from sqlalchemy.orm import Session
from pydantic import ValidationError
from uuid import UUID

from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate

def get_users(db: Session):
    return db.query(User).all()

def get_user(
    db: Session,
    user_id: UUID
):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_name(
    db: Session, 
    user_name: str
):
    return db.query(User).filter(User.name == user_name).first()

def create_user(
    db: Session,
    payload: UserCreate
):
    exists = get_user_by_name(db, payload.name)
    if exists:
        return None
    
    user = User(**payload.model_dump())
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except ValidationError:
        db.rollback()
        return None

def update_user(
    db: Session,
    user_id: UUID, 
    payload: UserUpdate, 
):
    user = get_user(db, user_id)
    if not user:
        return None
    
    exists = get_user_by_name(db, payload.name)
    if exists:
        return None
    
    data = payload.model_dump(exclude_unset=True)
    
    for field, value in data.items():
        setattr(user, field, value.value if hasattr(value, "value") else value)
    
    db.commit()
    db.refresh(user)
    return user

def delete_user(
    db: Session, 
    user_id: UUID
):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user