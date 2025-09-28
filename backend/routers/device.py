from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class DeviceCreate(BaseModel):
    name: str
    type: str
    greenhouseId: Optional[int] = None
    serialNumber: Optional[str] = ""
    deviceType: Optional[str] = "SOIL_MOISTURE"
    unit: Optional[str] = ""


class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    status: Optional[bool] = None
    serialNumber: Optional[str] = None
    deviceType: Optional[str] = None
    unit: Optional[str] = None


@router.get("/device/list")
def list_devices(greenhouseId: Optional[int] = None):
    devices = [
        {"id": 1, "name": "土壤温度", "type": "sensor", "status": True, "greenhouseId": 1, "serialNumber": "SN001", "deviceType": "SOIL_MOISTURE", "unit": "°C"},
        {"id": 2, "name": "土壤湿度", "type": "sensor", "status": True, "greenhouseId": 1, "serialNumber": "SN002", "deviceType": "SOIL_MOISTURE", "unit": "%"},
        {"id": 3, "name": "土壤PH值", "type": "sensor", "status": True, "greenhouseId": 1, "serialNumber": "SN003", "deviceType": "SOIL_MOISTURE", "unit": "pH"},
        {"id": 4, "name": "土壤氮含量", "type": "sensor", "status": True, "greenhouseId": 1, "serialNumber": "SN004", "deviceType": "SOIL_MOISTURE", "unit": "mg/kg"},
        {"id": 5, "name": "土壤电导率", "type": "sensor", "status": True, "greenhouseId": 1, "serialNumber": "SN005", "deviceType": "SOIL_MOISTURE", "unit": "mS/cm"},
        {"id": 6, "name": "摄像头", "type": "camera", "status": True, "greenhouseId": 1, "serialNumber": "CAM001", "deviceType": "CAMERA", "unit": ""},
        {"id": 7, "name": "风机", "type": "fan", "status": False, "greenhouseId": 1, "serialNumber": "FAN001", "deviceType": "CONTROL", "unit": ""},
        {"id": 8, "name": "加热器", "type": "heater", "status": False, "greenhouseId": 1, "serialNumber": "HEAT001", "deviceType": "CONTROL", "unit": ""},
        {"id": 9, "name": "水泵", "type": "irrigation", "status": True, "greenhouseId": 1, "serialNumber": "PUMP001", "deviceType": "CONTROL", "unit": ""},
        {"id": 10, "name": "补光灯", "type": "lamp", "status": False, "greenhouseId": 1, "serialNumber": "LAMP001", "deviceType": "CONTROL", "unit": ""},
    ]
    
    if greenhouseId:
        devices = [d for d in devices if d["greenhouseId"] == greenhouseId]
    
    return {
        "code": 200,
        "message": "success",
        "data": devices
    }


@router.post("/device")
def create_device(device: DeviceCreate):
    return {
        "code": 200,
        "message": "创建成功",
        "data": {
            "id": 11,
            **device.dict()
        }
    }


@router.put("/device/{device_id}")
def update_device(device_id: int, device: DeviceUpdate):
    return {
        "code": 200,
        "message": "更新成功",
        "data": {
            "id": device_id,
            **device.dict(exclude_unset=True)
        }
    }


@router.delete("/device/{device_id}")
def delete_device(device_id: int):
    return {
        "code": 200,
        "message": "删除成功",
        "data": None
    }


