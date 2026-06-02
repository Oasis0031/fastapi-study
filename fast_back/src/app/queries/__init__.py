from sqlalchemy import text

# 이메일 중복확인
EXISTS_MEMBER_QUERY = text("""
    SELECT *
    FROM TBL_MEMBERS
    WHERE MEMBER_EMAIL = :member_email
    AND MEMBER_PROVIDER = :provider
                           
""")