from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Targets(BaseModel):
    temp: float
    hum: float
    co2: float
    lux: float
    auto: bool | None = None


@router.post("/automation/targets")
def save_targets(payload: Targets):
    return {"code": 200, "message": "saved", "data": payload.dict()}


class DeviceToggle(BaseModel):
    key: str
    on: bool


@router.post("/automation/toggle")
def toggle_device(payload: DeviceToggle):
    return {"code": 200, "message": "toggled", "data": payload.dict()}


