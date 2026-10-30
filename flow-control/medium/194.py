# 문자열 압축
# 1. 문자열 입력
# 2. 문자열 순회
#    1) 전 문자와 비교 
#    2) 다음 비교를 위해 현재 문자 저장
# 3. 결과 출력

# 문자열 입력
s = input()

# 결과값 변수 초기화
result = ""

last_time_char = s[0]   # 마지막 문자 변수 초기화
count = 1   # 카운트 변수 초기화

# 문자열 순회 for문
for char in s[1:]:
    # 문자열 비교 if문
    if last_time_char == char:
        count += 1
    else:
        result += f"{last_time_char}{count}"
        count = 1
    # 문자 저장
    last_time_char = char

# 결과값 변수 저장
result += f"{last_time_char}{count}"
# 결과 출력
print(result)