# 별 찍기 삼각형
# 1. 줄 수 입력
# 2. 1 ~ n까지 반복 / 별 출력

# 줄 수 입력
n = int(input())

# 1 ~ n까지 반복하는 for문
for i in range(1, n + 1):
    # 별 출력
    print("*" * i)