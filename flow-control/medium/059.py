# 숫자 피라미드
# 1. n값 입력
# 2. 1부터 n까지 반복
#   i번째 줄 / 1~i까지 숫자 이여붙여 출력   

# n값 입력
n = int(input())

# 1부터 n까지 반복문
for i in range(1, n + 1):
    for number_line in range(1, i + 1):
        print(number_line, end="")
    print()     # 줄 바꿈
