import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        index=True,
        default=uuid.uuid4
    )
    name = Column(String, unique=True)
    invoices = relationship("Invoice", back_populates="user", cascade="all, delete-orphan")
