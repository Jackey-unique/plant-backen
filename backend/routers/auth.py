from fastapi import APIRouter

router = APIRouter()


@router.get("/auth/current")
def get_current_user():
    # No login mode: return a default user
    return {"code": 200, "message": "success", "data": {
        "id": 1,
        "username": "admin",
        "realName": "管理员",
        "roles": ["admin"]
    }}


