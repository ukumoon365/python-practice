# 단어 첫 글자 대문자 변환
# 1. 문자열 입력
# 2. 문자열 순회
#   1) 첫글자 대문자 변환
#   2) 공백시 다음 글자 대문자 변환
# 3. 결과 출력

# 문자열 입력
s = input()

# 결과값 변수 초기화
result = ""

# 플래그 변수 설정
found = True

# 문자열 순회 for문
for ch in s:
    # 첫글자 조건 판별 if문 
    if found:   # 첫글자 대문자 변환
        result += ch.upper()
    else:       # 조건에 맞지 않을 시 변환 하지않음
        result += ch
    if ch == " ":   # 공백이면 다음 글자 대문자 변환
        found = True
    else:           # 공백이 아니면 변환하지 않음
        found = False

# 결과 출력
print(result)