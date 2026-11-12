# 문자열 번호 매기기
# 1. 문자열 입력
# 2. 문자열, 인덱스 순회
# 3. 결과 출력

# 문자열 입력
text = input()

# 문자열, 인덱스 순회
for i, letter in enumerate(text, 1):
    # 결과 출력
    print(f"{i}.{letter}",end=" ")