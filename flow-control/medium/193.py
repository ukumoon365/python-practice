# 문자 종류 카운트
# 1. 문자열을 입력
# 2. 반복문으로 문자열 순회
#    각 문자를 대문자, 소문자, 숫자, 기타로 나누어 카운트
# 3. 결과 출력

# 문자열 입력
s = input()

# 각 종류 변수 초기화
upper = 0
lower = 0
digit = 0
other = 0

# 문자열 순회
for ch in s:
    # 문자 종류 분류 if문
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        other += 1

# 결과 출력
print(f"대문자: {upper}")
print(f"소문자: {lower}")
print(f"숫자: {digit}")
print(f"기타: {other}")