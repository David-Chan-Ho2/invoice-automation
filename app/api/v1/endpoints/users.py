from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.config.database import get_db
from app.schemas.users import UserCreate, UserResponse, UserUpdate
import app.crud.users as crud

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/", response_model=UserResponse)
def create_user(
    payload: UserCreate, 
    db: Session = Depends(get_db)
):
    user = crud.create_user(db, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User name already exists")
    return user

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User name already exists")
    return user

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: UUID, 
    payload: UserUpdate, 
    db: Session = Depends(get_db)
):
    user = crud.update_user(db, user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User Deleted"}