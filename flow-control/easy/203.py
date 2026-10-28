# 이진수 1의 개수
# 1. 정수 입력
# 2. 십진수가 더 이상 나눠지지 않을 때까지 반복
#   1) 2로 나누어 나머지가 1일때의 개수 카운트
# 3. 결과 출력

# 정수 입력
n = int(input())

# 카운트 변수 초기화
count = 0
# 십진수 변수 
quotient = n

# 십진수가 더 나눠지지 않을 때까지 반복 while문
while quotient > 0:
    # 2진수로 변환 
    if quotient % 2:
        count += 1  # 나머지값 1 개수 카운트
    quotient //= 2  # 자릿수 줄이기

# 결과 출력
print(count)