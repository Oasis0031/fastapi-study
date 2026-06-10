from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from app.services.rag_service import RagService, get_rag_service
from app.dependencies.auth_dependency import get_auth_context
from app.schemas.auth_schema import AuthContextDTO

router = APIRouter()

# pdf 업로드 -> S3 저장 -> rag anything 전처리 -> postsql vector DB 저장
@router.post(
    "/ingest-document",
    summary="pdf upload, rag processing"
)
async def ingest_document(
    file: UploadFile = File(...),
    auth_context: AuthContextDTO = Depends(get_auth_context),
    rag_service: RagService = Depends(get_rag_service)
):
    member_id = auth_context.member_claims.id
    await rag_service.ingest_document(file, member_id)

# pdf 업로드 파일 질문 