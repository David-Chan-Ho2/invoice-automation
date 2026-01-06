import uuid

from sqlalchemy import Column,  Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.schemas.invoices import StatusEnum
from app.config.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        index=True,
        default=uuid.uuid4
    )
    status = Column(
        Enum(StatusEnum),
        nullable=False,
        default=StatusEnum.PEND
    )
    user_id = Column(
        UUID(as_uuid=True), 
        ForeignKey("users.id"),
        nullable=False
    )
    
    user = relationship("User", back_populates="invoices")
