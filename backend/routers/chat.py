from fastapi import APIRouter
from pydantic import BaseModel
from services.langchain_service import ask_ai

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

class ChatRequest(BaseModel):
    user_query: str
    session_id: str = "user1"

@router.post("/")
def chat(request: ChatRequest):
    response = ask_ai(request.user_query, request.session_id)
    return {"response": response}