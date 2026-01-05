from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional, Annotated

from app.schemas.invoices import InvoiceResponse

class UserCreate(BaseModel):
    name: Annotated[str, Field(max_length=16)]
    
class UserUpdate(BaseModel):
    name: Annotated[Optional[str], Field(max_length=16)] = None
    
class UserResponse(BaseModel):
    id: int
    name: str
    invoices: List[InvoiceResponse]
    
    model_config = ConfigDict(from_attributes=True)
    