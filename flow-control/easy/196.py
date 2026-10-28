# 모음 제거
# 1. 문자열 입력
# 2. 문자열 순회
#    1) 모음 판별
#       1. 모음 제거
# 3. 결과 출력

# 문자열 입력
s = input()

# 결과값 변수 초기화
result = ""

# 모음 리스트
vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# 문자열 순회 for문
for ch in s:
    # 모음 판별 if문
    if ch in vowel_list:
        continue
    else:
        result += ch

# 결과 출력
print(result)