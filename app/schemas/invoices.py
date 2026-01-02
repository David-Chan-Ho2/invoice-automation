from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional

class StatusEnum(Enum):
    PEND = 'Pending'
    PAID = 'Paid'
    CANCEL = 'Cancelled'

class Invoice(BaseModel):
    id: int
    status: StatusEnum

class InvoiceCreate(BaseModel):
    pass

class InvoiceUpdate(BaseModel):
    status: Optional[StatusEnum] = None
    
class InvoiceResponse(BaseModel):
    id: int
    status: StatusEnum

    model_config = ConfigDict(from_attributes=True)

