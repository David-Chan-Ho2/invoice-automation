from fastapi import APIRouter

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"]
)

invoices = [{"id": 1, "name": "hello"}]

@router.get("/")
def read_invoices():
    return invoices

@router.get("/{invoice_id}")
def read_invoice(invoice_id: int):
    return invoices[invoice_id]

@router.post("/")
def add_post(name: str):
    new_id = len(invoices) + 1
    invoices.append({"id": new_id, "name": name})
    return invoices[new_id - 1]

@router.put("/{invoice_id}")
def update_invoice(invoice_id: int, name: str):
    global invoices
    update_invoice = [i for i in invoices if i["id"] == invoice_id][0]
    update_invoice["name"] = name
    return update_invoice    
    
@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int):
    global invoices
    invoices = [i for i in invoices if i["id"] != invoice_id]
    return {"message": "invoice removed"}