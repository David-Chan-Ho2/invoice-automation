from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional

from uuid import UUID

class StatusEnum(str, Enum):
    PEND = 'Pending'
    PAID = 'Paid'
    CANCEL = 'Cancelled'

class InvoiceCreate(BaseModel):
    status: StatusEnum = StatusEnum.PEND
    user_id: UUID
    
class InvoiceUpdate(BaseModel):
    status: Optional[StatusEnum] = None
    
class InvoiceResponse(BaseModel):
    id: UUID
    status: StatusEnum
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)

