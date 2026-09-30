# 직각 삼각형 (오른쪽 정렬)
# 1. 줄 수 n을 입력 받는다
# 2. 반복문을 통해 줄을 세우고 i번째 줄에 공백 (n - i)개와 별 i개를 출력한다

# 줄 수 입력
n = int(input())

# 별 출력 반복문
for star_line in range(1, n + 1):
    print(" " * (n - star_line) + "*" * star_line)