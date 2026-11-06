# 부분문자열 위치
# 1. 문자열, 타겟 입력
# 2. 타켓 유무 확인
# 3. 결과 출력

# 문자열, 타켓 입력
text = input()
target = input()

# 문자열 안에 타켓 존재 유무 판별 if문 / 결과 출력
print(text.index(target) if target in text else "없음")