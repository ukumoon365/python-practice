# 소수 판별
# 1. 2 이상의 정수 n를 입력 받는다
# 2. 반복문으로 소수 판별
# 3. 결과 출력

num = int(input())

# is_prime 값 True 초기화
is_prime = True 

# 소수 판별 반복문
for i in range(2, num):
  if num % i == 0:      
    is_prime = False    # 소수가 아님
    break   # 반복 종료

# 결과 출력
if is_prime:
  print(f"{num}은(는) 소수입니다")
else: # 소수가 아닐 경우
  print(f"{num}은(는) 소수가 아닙니다 ({num} = {i} x {num//i})")