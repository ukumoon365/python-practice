# 부분문자열 포함 여부
# 1. 문자열, 부분문자열 입력
# 2. 포함 여부 확인 후 출력

# 문자열 입력
text = input()
# 부분 문자열 입력
sub = input()

# 결과 출력
print("포함" if sub in text else "미포함")