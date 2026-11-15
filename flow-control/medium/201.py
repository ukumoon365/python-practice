# 소인수분해
# 1. 정수 입력
# 2. 정수의 값이 1이 될 때까지 반복
#    약수 (2부터)로 n을 나눈 나머지가 0이 될 때 까지 반복
#    소인수의 값을 리스트에 저장
# 3. 소인수 리스트를 순회하며 소인수를 x를 연결하여 출력

# 정수 입력
n = int(input())

# 자릿수 변수 초기화
divisor = 2
# 소인수 값 저장 리스트
prime_factors = []

# 정수의 값이 1이 될 때까지 반복 while문
while n > 1:
    while n % divisor == 0:
        prime_factors.append(divisor)
        n //= divisor
    divisor += 1

# 결과 출력
print(" x ".join(map(str, prime_factors)))