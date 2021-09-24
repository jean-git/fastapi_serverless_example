from typing import Optional
from fastapi import APIRouter

router = APIRouter()

@router.get("")
@router.get("/")
async def get_users():
    return {"message": f"Users!"}


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{id}")
async def get_users(id: str, q: Optional[str] = None):
    return {"message": f"Users! ID: {id}"}


