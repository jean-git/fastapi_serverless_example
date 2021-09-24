from fastapi import APIRouter

from .routes import users
from .routes import companies

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(companies.router, prefix="/companies", tags=["Companies"])