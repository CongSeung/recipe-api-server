class Config : 
    # 이 부분은 시드 값으로 외부 유출 XX
    JWT_SECRET_KEY = 'highhhhrqllzq1206'

    # True는 기본적으로 토큰 유지 시간제한 180초, False 시간제한 없음
    JWT_ACCESS_TOKEN_EXPIRES = False

    PROPAGATE_EXEPTIONS = True