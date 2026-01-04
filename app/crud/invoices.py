from sqlalchemy.orm import Session

from app.models.invoices import Invoice
from app.schemas.invoices import InvoiceCreate, InvoiceUpdate

def get_invoices(db: Session, limit: int, offset: int):
    return db.query(Invoice).limit(limit).offset(offset).all()

def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoice).where(Invoice.id == invoice_id).first()
    
def create_invoice(db: Session, payload: InvoiceCreate):
    invoice = Invoice(**payload.model_dump()) 
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

def update_invoice(
    db: Session,
    invoice_id: int,
    payload: InvoiceUpdate,
):
    invoice = db.query(Invoice).where(Invoice.id == invoice_id).first()
    
    if not invoice:
        return None
    
    data = payload.model_dump(exclude_unset=True)
    
    for field, value in data.items():
        setattr(invoice, field, value.value if hasattr(value, "value") else value)

    db.commit()
    db.refresh(invoice)
    
    return invoice

def delete_invoice(db: Session, invoice_id: int):
    invoice = db.query(Invoice).where(Invoice.id == invoice_id).first()
    
    if invoice:
        db.delete(invoice)
        db.commit()
        
    return invoice