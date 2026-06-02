from fastapi import APIRouter, Depends
from app.repositories.member_repository import get_member_repository

router = APIRouter()

@router.post(
    "/join",
    summary="로컬 회원가입"
)
def join():
    pass


@router.post(
    "/test",
    summary="레포지토리 테스트"
)
async def test(
    member_email: str,
    member_provider: str,
    member_repository = Depends(get_member_repository)
):
    await member_repository.exists_member(member_email, member_provider)

@router.post(
  "/test",
  summary="레포지토리 테스트"
)
async def test(
  member_respository = Depends(get_member_repository)
):
  await member_respository.find_members()
async def test(
    member_repository = Depends(get_member_repository)
):
    await member_repository.find_member_by_id(id)