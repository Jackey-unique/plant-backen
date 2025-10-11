from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class GreenhouseCreate(BaseModel):
    name: str
    address: Optional[str] = ""
    area: float
    boxNo: Optional[str] = ""
    accessToken: Optional[str] = ""


class GreenhouseUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    area: Optional[float] = None
    boxNo: Optional[str] = None
    accessToken: Optional[str] = None


@router.get("/greenhouse/list")
def list_greenhouses():
    return {
        "code": 200,
        "message": "success",
        "data": [
            {"id": 1, "name": "一号棚", "area": 1200, "address": "陕西省西安市", "boxNo": "BOX001", "status": 1, "createTime": "2024-01-01 10:00:00"},
            {"id": 2, "name": "二号棚", "area": 950, "address": "上海市", "boxNo": "BOX002", "status": 1, "createTime": "2024-01-02 10:00:00"},
        ],
    }


@router.post("/greenhouse")
def create_greenhouse(greenhouse: GreenhouseCreate):
    return {
        "code": 200,
        "message": "创建成功",
        "data": {
            "id": 3,
            **greenhouse.dict()
        }
    }


@router.put("/greenhouse/{greenhouse_id}")
def update_greenhouse(greenhouse_id: int, greenhouse: GreenhouseUpdate):
    return {
        "code": 200,
        "message": "更新成功",
        "data": {
            "id": greenhouse_id,
            **greenhouse.dict(exclude_unset=True)
        }
    }


@router.delete("/greenhouse/{greenhouse_id}")
def delete_greenhouse(greenhouse_id: int):
    return {
        "code": 200,
        "message": "删除成功",
        "data": None
    }


