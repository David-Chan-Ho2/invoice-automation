from pydantic import BaseModel, ConfigDict
from typing import List, Optional

from app.schemas.invoices import InvoiceResponse

class UserCreate(BaseModel):
    name: str
    
class UserResponse(BaseModel):
    id: int
    name: str
    invoices: List[InvoiceResponse]
    
    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(BaseModel):
    name: Optional[str] = None