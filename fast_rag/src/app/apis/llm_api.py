import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI

from app.schemas.common_schema import ApiResponseDTO
from app.schemas.auth_schema import AuthContextDTO
from app.dependencies.auth_dependency import get_auth_context
from app.schemas.llm_schema import ChatRequestDTO

router = APIRouter()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
llm_client = OpenAI(
  api_key=OPENAI_API_KEY)

@router.post(
  "/chat-bot",
  summary="llm 모델 응답",
  response_model=ApiResponseDTO
)

async def chat(
    chat_request_dto: ChatRequestDTO,
    auth_context: AuthContextDTO = Depends(get_auth_context)
):
    print(auth_context)
    
    result = llm_client.responses.create(
        temperature=0.5,
        model="gpt-4",
        input=chat_request_dto.question
    )
    
    return ApiResponseDTO(
      success=True,
      message="로그아웃 성공",
      data=result.output_text
    )
    
@router.post(
  "/chat-bot/stream",
  summary="llm 모델 stream 응답",
)
async def chat_stream(
  chat_request_dto: ChatRequestDTO
):
    def generate():
        with llm_client.responses.stream(
            model="gpt-5",
            input=chat_request_dto.question
        ) as stream:
            for text in stream.text_stream:
                yield text

    return StreamingResponse(generate(), media_type="text/event-stream")