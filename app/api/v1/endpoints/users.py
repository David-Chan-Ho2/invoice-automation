from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.models.users import User
from app.api.deps import get_db
from app.schemas.users import UserCreate, UserResponse
import app.crud.users as crud

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, payload)


