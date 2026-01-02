from sqlalchemy import Column, Integer, Enum

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
