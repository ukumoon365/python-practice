# 다이아몬드
# 1. 줄 수 n 입력 받기
# 2. 1부터 n까지 삼각형으로 별 출력
# 3. n부터 1까지 역삼각형으로 별 출력

# 정수 입력
n = int(input())

# 다이아몬드 별 출력 for문
for triangle in range(1, n + 1):
    print(" " * (n - triangle) + "*" * (2 * triangle - 1))
for inverted in range(n - 1, 0, -1): #n-1부터 1까지 역삼
    print(" " * (n - inverted) + "*" * (2 * inverted - 1))