from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AskPayload(BaseModel):
    question: str


@router.post("/ai/ask")
def ai_ask(payload: AskPayload):
    # Placeholder answer
    return {"code": 200, "message": "success", "data": {
        "answer": "这是基于知识库与策略的参考答案（示例）。"
    }}


