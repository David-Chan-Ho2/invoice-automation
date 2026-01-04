from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.invoices import InvoiceCreate, InvoiceResponse, InvoiceUpdate
from app.crud import invoices as crud, users
from app.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[InvoiceResponse])
def read_invoices(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return crud.get_invoices(db, limit, offset)

@router.get("/{invoice_id}", response_model=InvoiceResponse)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    return crud.get_invoice(db, invoice_id)

@router.post("/", response_model=InvoiceResponse)
def add_invoice(payload: InvoiceCreate, db: Session = Depends(get_db)):
    if not users.get_user(payload.user_id, db):
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_invoice(db, payload)

@router.patch("/{invoice_id}", response_model=InvoiceResponse)
def update_invoice(
    invoice_id: int,
    payload: InvoiceUpdate, 
    db: Session = Depends(get_db)
):
    invoice = crud.update_invoice(db, invoice_id, payload)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = crud.delete_invoice(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=304, detail="Invoice not found")
    return {"message": "invoice removed"}
