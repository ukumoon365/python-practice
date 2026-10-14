# 누적 곱 계산
# 1. 정수 입력
# 2. count번 반복 
#   1) 정수 입력
#   2) 누적곱 계산
# 3. 결과 출력

# 정수 입력
count = int(input())

# 결과값 변수 초기화
result = 1 

# count번 반복 for문
for i in range(1, count + 1):  
    num = int(input())  # 정수 입력
    result *= num  # 누적곱 계산

# 결과 출력
print(f"누적 곱: {result}")
    