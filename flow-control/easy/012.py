# 비밀번호 확인
# 1. 설정 비밀번호 초기화
# 2. 비밀번호 입력
# 3. 설정 비밀번호와 입력된 비밀번호 비교 및 결과 출력

# 설정 비밀번호 초기화
password = "python123"

# 비밀번호 입력
user_input = input()

# 설정된 비밀번호(password)와 입력된 비밀번호(user_input)의 일치 여부 판단
if user_input == password:
    print("로그인 성공")
else: # 설정된 비밀번호(password)와 같지 않은 모든 입력값(user_input)
    print("비밀번호 오류")
    print("다시 시도하세요")
