from enum import Enum

class MemberProvider(str, Enum):
    LOCAL = "LOCAL"
    KAKAO = "KAKAO"
    NAVER = "NAVER"
    GOOGLE = "GOOGLE"