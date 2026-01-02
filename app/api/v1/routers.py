from fastapi import APIRouter
from .endpoints import invoices

router = APIRouter()

router.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])