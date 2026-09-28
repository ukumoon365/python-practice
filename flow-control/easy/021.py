# 동전 변환
# 1. 금액 입력
# 2. 현재 금액 출력
# 3. 금액를 각 동전 단위에 맞춰 개수 세기
# 4. 총 동전 개수 계산
# 5. 결과 출력


# 금액 입력
amount = int(input())

#계산 전 출력
print(f"{amount}원 → 동전 변환:")

# 각 동전에 맞춰 나누어 개수 세기
five_hundred = amount // 500  # 500으로 나눈 몫 -> 500원 개수 
amount %= 500  # 500으로 나눈 나머지 -> 잔여 금액
hundred = amount // 100
amount %= 100
fifty = amount // 50
amount %= 50
ten = amount // 10
# 10 미만은 버리기에 나머지 구하지 않음

# 총 동전 개수 
total_number = five_hundred + hundred + fifty + ten

# 결과 출력
print(f"500원: {five_hundred}개\n100원: {hundred}개\n50원: {fifty}개\n10원: {ten}개")
print(f"총 동전 수: {total_number}개")