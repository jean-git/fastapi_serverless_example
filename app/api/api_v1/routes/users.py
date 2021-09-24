from typing import Optional
from fastapi import APIRouter

router = APIRouter()

list_users = [{"id": 1, "nome": "User 1"}, {"id": 2, "nome": "User 2"}]

@router.get("")
@router.get("/")
async def get_users():
    return list_users


@router.get("/me", tags=["users"])
async def read_user_me():
    return list_users[0]


@router.get("/{id}")
async def get_users(id: int):
    res = next((item for item in list_users if item["id"] == id), {})

    return res
