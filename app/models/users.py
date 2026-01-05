from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    invoices = relationship("Invoice", back_populates="user", cascade="all, delete-orphan")
