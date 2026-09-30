# 로그인 시스템
# 1. 아이디, 비밀번호 입력
# 2. 입력값에 따라 로그인 여부 판별 및 결과 출력

# 아이디, 비밀번호 입력
user_id = input()
password = input()

# 아이디 판별 if문
if user_id == "admin":
    # 비밀번호 판별 if문
    if password == "1234":
        print("로그인 성공!")
    else: # id는 맞지만 password가 틀릴 경우
        print("비밀번호가 틀렸습니다.")
else: # id가 틀렸을 경우
    print("ID가 존재하지 않습니다.")