# 전기 요금 계산
# 1. 전기 사용량 입력
# 2. 전기 사용량 비교 
#   1) 각  사용량에 맞는 요금 계산
# 3. 부가세, 총 납부 금액 계산
# 4. 결과 출력

# 전기 사용량 입력
usage = int(input())

# 전기 사용량 비교 if문
if usage <= 100:
    charge = usage * 60
elif 100 < usage <= 200:
    charge = 100 * 60 + (usage - 100) * 120
else:   # 전기 사용량 200 초과
    charge = 100 * 60 + 100 * 120 + (usage - 200) * 190

# 부가세 계산
tax = int(charge * 0.1)
# 총 납부 금액 계산
total_price = charge + tax

# 결과 출력
print(f"전기 요금: {charge}원")
print(f"부가세 (10%): {tax}원")
print(f"총 납부 금액: {total_price}원")