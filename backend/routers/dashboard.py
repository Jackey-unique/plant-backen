from fastapi import APIRouter
from typing import List
import random
import time

router = APIRouter()


@router.get("/dashboard/overview")
def dashboard_overview():
    return {
        "code": 200,
        "message": "success",
        "data": {
            "sensors": {
                "temp": round(random.uniform(20, 30), 1),
                "hum": round(random.uniform(50, 80), 1),
                "co2": random.randint(600, 1000),
                "lux": random.randint(20000, 40000),
            },
            "devices": {
                "fan": False,
                "heater": False,
                "irrigation": True,
                "lamp": False,
            }
        }
    }


@router.post("/device-data/greenhouse/{greenhouse_id}")
def get_device_real_time_data(greenhouse_id: int, serial_numbers: List[str]):
    """获取设备实时数据"""
    data = []
    for sn in serial_numbers:
        # 模拟不同传感器的数据
        if "SN001" in sn:  # 土壤温度
            value = round(random.uniform(15, 35), 1)
        elif "SN002" in sn:  # 土壤湿度
            value = round(random.uniform(30, 90), 1)
        elif "SN003" in sn:  # 土壤PH值
            value = round(random.uniform(5.5, 8.5), 1)
        elif "SN004" in sn:  # 土壤氮含量
            value = round(random.uniform(80, 250), 1)
        elif "SN005" in sn:  # 土壤电导率
            value = round(random.uniform(0.3, 3.0), 2)
        else:
            value = round(random.uniform(0, 100), 1)
        
        data.append({
            "id": sn,
            "value": value,
            "timestamp": int(time.time() * 1000)
        })
    
    return {
        "code": 200,
        "message": "success",
        "data": data
    }


@router.get("/device-data/soil/{serial_number}/stats")
def get_device_history_data(serial_number: str):
    """获取设备历史数据"""
    # 生成24小时的历史数据
    data = []
    current_time = int(time.time() * 1000)
    
    for i in range(24):
        timestamp = current_time - (23 - i) * 3600000  # 每小时一个数据点
        
        # 根据设备类型生成不同的数据
        if "SN001" in serial_number:  # 土壤温度
            base_value = 25
            variation = random.uniform(-5, 5)
        elif "SN002" in serial_number:  # 土壤湿度
            base_value = 65
            variation = random.uniform(-15, 15)
        elif "SN003" in serial_number:  # 土壤PH值
            base_value = 7.0
            variation = random.uniform(-1, 1)
        elif "SN004" in serial_number:  # 土壤氮含量
            base_value = 150
            variation = random.uniform(-30, 30)
        elif "SN005" in serial_number:  # 土壤电导率
            base_value = 1.5
            variation = random.uniform(-0.5, 0.5)
        else:
            base_value = 50
            variation = random.uniform(-20, 20)
        
        value = round(base_value + variation, 2)
        
        data.append({
            "createTime": timestamp,
            "value": value
        })
    
    return {
        "code": 200,
        "message": "success",
        "data": data
    }


@router.get("/monitor/ys-token")
def get_ys_access_token():
    """获取萤石云访问令牌"""
    return {
        "code": 200,
        "message": "success",
        "data": {
            "accessToken": "at.1234567890abcdef",
            "expireTime": int(time.time() + 3600) * 1000
        }
    }


