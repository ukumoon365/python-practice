# 괄호 짝 검사
# 1. 문자열 입력
# 2. 문자열 순회
#     1) "(",")" 판별
#       1. 괄호 개수 카운트
# 3. 괄호 개수 비교    
#     1) 두개의 개수가 같으면 / 올바름
#     1) 다르면 / 올바르지 않음
# 4. 결과 출력

# 문자열 입력
s = input()

# 괄호 개수 카운트 변수 초기화
open_parenthesis = 0
close_parenthesis = 0

# 문자열 순회 for문
for ch in s:
    # 괄호 개수 카운트 if문
    if ch == "(":
        open_parenthesis += 1
    elif ch == ")":
        close_parenthesis += 1

# 괄호 개수 비교 if문 / 결과 출력
if open_parenthesis  == close_parenthesis:
    print("올바름")
else:
    print("올바르지 않음")