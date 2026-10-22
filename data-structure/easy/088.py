# set에 원소 추가
# 1. 정수 입력
# 2. n번 반복
#   1) 단어 입력
#   2) set에 추가
# 3. set 원소 정렬
# 4. 결과 출력

# 정수 입력
n = int(input())

# 단어 set 초기화
word_set = set()

# n번 반복 for문
for _ in range(n):
    # 단어 입력
    word = input()
    # 빈 set에 추가
    word_set.add(word)

# set 정렬
sorted_set = sorted(word_set)

# 결과 출력 
print(" ".join(sorted_set))
