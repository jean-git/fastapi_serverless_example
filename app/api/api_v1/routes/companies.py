from typing import Optional
from fastapi import APIRouter

router = APIRouter()

list_companies = [{"id": 1, "nome": "Company 1"}, {"id": 2, "nome": "Company 2"}]

@router.get("")
@router.get("/")
async def get_companies():
    return list_companies


@router.get("/{id}")
async def get_company(id: int):
    res = next((item for item in list_companies if item["id"] == id), {})

    return res
