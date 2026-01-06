from sqlalchemy.orm import Session
from pydantic import ValidationError
from app.models.invoices import Invoice
from app.schemas.invoices import InvoiceCreate, InvoiceUpdate
from uuid import UUID

from app.crud import users

def get_invoices(
    db: Session, 
    limit: int, 
    offset: int
):
    return db.query(Invoice).limit(limit).offset(offset).all()

def get_invoices_all(db: Session):
    return db.query(Invoice).all()

def get_invoice(
    db: Session, 
    invoice_id: UUID
):
    return db.query(Invoice).where(Invoice.id == invoice_id).first()
    
def create_invoice(
    db: Session, 
    payload: InvoiceCreate
):
    user = users.get_user(db, payload.user_id)
    if not user:
        return None

    invoice = Invoice(**payload.model_dump()) 
    try:
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice
    except ValidationError:
        return None

def update_invoice(
    db: Session,
    invoice_id: UUID,
    payload: InvoiceUpdate,
):
    invoice = get_invoice(db, invoice_id)
    if not invoice:
        return None
    data = payload.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(invoice, field, value.value if hasattr(value, "value") else value)
    db.commit()
    db.refresh(invoice)
    return invoice

def delete_invoice(
    db: Session, 
    invoice_id: UUID
):
    invoice = get_invoice(db, invoice_id)
    if invoice:
        db.delete(invoice)
        db.commit()
    return invoice