# 특정 길이의 단어만 추출
# 1. 문자 길이를 입력
# 2. words 리스트를 순회하며 n과 같은 문자 길이만 리스트에 저장
# 3. 결과 출력

# 단어 리스트
words = ["apple", "cat", "banana", "fig", "kiwi", "lemon", "pear"]

# 정수 입력
n = int(input())

selected_words = [word for word in words if len(word) == n]     # 문자 길이가 n과 같은 문자만 저장

# 결과 출력
print(*selected_words)      # 언패킹으로 공백 구분으로 출력