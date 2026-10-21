# 단어 빈도 카운트
# 1. 단어 입력 (공백 구분)
# 2. 리스트 순회
#   1) 단어 카운트, 딕셔너리 저장
# 3. 딕셔너리 순회
#   1) 항목 출력

# 단어 입력
words = input().split()

# 카운트 딕셔너리 초기화
counts = {}

# 리스트 순회 for문
for word in words:
    # 딕셔너리 저장
    counts[word] = counts.get(word, 0) + 1

# 딕셔너리 순회 for문
for word, count in counts.items():
    # 항목 출력
    print(f"{word}: {count}")