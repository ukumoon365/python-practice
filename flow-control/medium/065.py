# 역 숫자 피라미드
# 1. 정수 입력
# 2. 역 숫자 피라미드 출력 반복문

# 정수 입력
n = int(input())

# 역 숫자 피라미드 출력 for문
for i in range(n, 0, -1):   # 줄 세우기
    # n부터 -1씩 역순으로 숫자 출력
    number_line = "" . join (str(reverse_number) for reverse_number in range(i, 0, -1))
    print(number_line) 