from fastapi import APIRouter

from .endpoints import invoices, users

router = APIRouter()

router.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])
router.include_router(users.router, prefix="/users", tags=["Users"])
