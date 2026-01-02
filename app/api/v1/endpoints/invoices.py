from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.schemas.invoices import Invoice, InvoiceCreate, InvoiceResponse, InvoiceUpdate
from app.crud import invoices as crud
from app.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[InvoiceResponse])
def read_invoices(db: Session = Depends(get_db)):
    return crud.get_invoices(db)

@router.get("/{invoice_id}", response_model=Invoice)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    return crud.get_invoice(db, invoice_id)

@router.post("/", response_model=InvoiceResponse)
def add_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice)

@router.put("/{invoice_id}", response_model=Invoice)
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
