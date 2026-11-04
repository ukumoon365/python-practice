# 끝 검사
# 1. 문자열, 검사 문자열 입력
# 2. 결과 출력 / 문자열의 시작 문자가 suffix와 같다면 yes / 아니면 no

# 문자열 입력
text = input()
# 찾을 문자열 입력
suffix = input()

# 결과 출력
print("yes" if text.endswith(suffix) else "no")