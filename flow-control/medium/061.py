# 역 삼각형 별 찍기
# 1. 줄 수 n을 입력 받는다
# 2. 첫 줄은 별 n개, 마지막 줄은 별 1개가 출력하여 역삼각형 모양으로 출력

# 줄 수 입력
n = int(input())

# 별 출력 반복문
for star_line in range(n, 0, -1):       # 반복문으로 n개 만큼 줄 세우기
    for _ in range(star_line):     # n개부터 -1씩 빼가며 1개까지 별 출력
        print("*", end="")
    print()     # 줄 바꿈
