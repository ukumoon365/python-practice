# 계단 요금
# 1. 층 수 입력 
# 2. 요금 입력 
# 3. n번 반복
#       1) 가격 계산 / 총합 계산 / 각 층 결과 출력

# 층 수 입력
n = int(input())

# 총합계 변수 초기화
total_sum_price = 0

# n번 반복 for문
for i in range(1, n + 1):
    price = 100 * i # 가격 계산
    total_sum_price += price    # 총합 계산
    print(f"{i}층: {price}원 (누적: {total_sum_price}원)")  # 각 층 결과 출력