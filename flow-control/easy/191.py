# 이메일 유효성 검사
# 1. 문자열 입력
# 2. 문자열 순회
#       1) 플래그 변수로 이메일 유효성 검사
# 3. 결과 출력

# 이메일 입력
s = input()

# 플래그 변수 기본값 설정
found_at = False
found_dot = False

# 문자열 순회 for문
for string in s:
    # 이메일 유효성 검사 if문 (플래그 변수) 
    if string == "@":
        found_at = True
    if string == ".":
        found_dot = True

# 결과 출력
if found_at and found_dot:  # 모든 조건 만족 / 유효
    print("유효")
else:   # 한개의 조건이라도 만족 못함 / 무효
    print("무효")