# 홀수만 출력
# 1. 정수 입력
# 2. n번 반복
# 3. 홀수만 출력

# 정수 입력
n = int(input())

# n번 반복 for문
for i in range(1, n+1):
    if i % 2 == 1: # 홀수 판별 if문
        print(i) # 출력
