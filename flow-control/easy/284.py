# 자릿수의 합
# 1. 정수 입력
# 2. 각 자릿수 합
# 3. 결과 출력

# 정수 입력
number = int(input())

# 결과값 변수 초기화
total_sum = 0

# 양의 정수 판별 및 정수 입력 while문
while number <= 0:
    print("양의 정수를 입력하세요")
    number = int(input())

 
# 자릿수 분해 및 합산 while문
while number > 0:
    total_sum += number % 10    # 자릿수 누적합
    number //= 10   # 자릿수 분해

# 결과 출력
print(total_sum)