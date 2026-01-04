from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional

class StatusEnum(str, Enum):
    PEND = 'Pending'
    PAID = 'Paid'
    CANCEL = 'Cancelled'

class InvoiceCreate(BaseModel):
    status: StatusEnum = StatusEnum.PEND
    user_id: int
    
class InvoiceUpdate(BaseModel):
    status: Optional[StatusEnum] = None
    
class InvoiceResponse(BaseModel):
    id: int
    status: StatusEnum
    user_id: int

    model_config = ConfigDict(from_attributes=True)

