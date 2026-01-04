from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.schemas.invoices import StatusEnum
from app.config.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(
        Enum(StatusEnum),
        nullable=False,
        default=StatusEnum.PEND
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("User", back_populates="invoices")
