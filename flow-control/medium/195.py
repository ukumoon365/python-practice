# 두 문자열 교차 출력
# 1. 두 문자열을 입력
# 2. 두 문자열 중 긴 문자열의 선택
# 3. 선택된 문자열 순회
#    1) 교차로 result에 값 추가
# 4. 결과 출력

# 두 문자열 입력
s1 = input()
s2 = input()

# 결과값 변수 초기화
result = ""

# 더 긴 문자열 선택 if문
if len(s1) < len(s2):
    len_str = len(s2)
else:
    len_str = len(s1)

# 문자열 순회 for문
for i in range(len_str):
    # 문자열 교차 저장 if문
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[i]

# 결과 출력
print(result)