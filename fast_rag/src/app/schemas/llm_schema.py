from pydantic import BaseModel

class ChatRequestDTO(BaseModel):
    system_prompt: str | None = "당신은 친절한 AI 어시스턴스입니다."
    question: str

