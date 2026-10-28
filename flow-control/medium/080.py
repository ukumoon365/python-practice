# 1~n 합계
# 1. 정수 입력
# 2. 1 ~ n 까지 반복
#       1) 합산
# 3. 결과 출력

# 정수 입력
n = int(input())

# 결과값 변수 초기화
result = 0

# 1부터 n까지 반복 for문
for i in range(1, n + 1):
    # 합산
    result += i

# 결과 출력
print(f"1부터 {n}까지의 합: {result}")