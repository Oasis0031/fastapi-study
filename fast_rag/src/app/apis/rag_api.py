import traceback
from fastapi import APIRouter, Depends, File, UploadFile
from app.services.rag_service import RagService, get_rag_service
from app.dependencies.auth_dependency import get_auth_context
from app.schemas.auth_schema import AuthContextDTO
from app.schemas.common_schema import ApiResponseDTO

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

    if not file.filename.lower().endswith(".pdf") or file.content_type != "application/pdf":
        return ApiResponseDTO(
            success=False,
            message="pdf 파일만 업로드 가능합니다."
        )

    try:
        await rag_service.ingest_document(file, member_id)
    except Exception:
        traceback.print_exc()
        raise

@router.get(
    "/query",
    summary="Rag 질문"
)
async def query_rag(
    question: str,
    document_id: int,
    auth_context: AuthContextDTO = Depends(get_auth_context),
    rag_service: RagService = Depends(get_rag_service),
):
    return await rag_service.query(question, document_id)

# pdf 업로드 파일 질문 
