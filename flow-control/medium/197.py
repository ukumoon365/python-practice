# 카멜케이스 변환

# 1. 문자열 입력
# 2. 문자열 순회
#    "_"의 다음 문자는 대문자 변환 후 추가 (첫 글자 제외) / 
#    "_" 삭제 -> "_"은 result에 추가 하지 않음 / 나머지 값은 그대로 추가
# 3. 결과 출력

# 문자열 입력
s = input()

# 결과값 변수 초기화
result = ""

# 첫글자 변수 초기화
prev_char = s[0]

# 문자열 순회
for char in s:
    # 카멜케이스 변환 if문
    if prev_char == "_":
        result += char.upper()
    elif char != "_":
        result += char
    prev_char = char

# 결과 출력
print(result)