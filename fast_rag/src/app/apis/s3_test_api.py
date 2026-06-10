from fastapi import APIRouter, Depends, File, UploadFile
from app.services.s3_service import S3Service, get_s3_service
from app.schemas.file_schema import FileUploadResponseDTO

router = APIRouter()

# S3 동작 확인용 임시 테스트 라우터 (인증 없음)

@router.post("/upload", response_model=FileUploadResponseDTO)
async def test_upload(
    file: UploadFile = File(...),
    s3_service: S3Service = Depends(get_s3_service)
):
    return await s3_service.upload_file(file, "test")


@router.get("/url/{key:path}")
async def test_get_url(
    key: str,
    s3_service: S3Service = Depends(get_s3_service)
):
    return {"url": await s3_service.get_url(key)}


@router.get("/download/{key:path}")
async def test_get_download_url(
    key: str,
    s3_service: S3Service = Depends(get_s3_service)
):
    return {"url": await s3_service.get_download_url(key)}


@router.delete("/{key:path}")
async def test_delete(
    key: str,
    s3_service: S3Service = Depends(get_s3_service)
):
    await s3_service.delete_file(key)
    return {"deleted": key}
