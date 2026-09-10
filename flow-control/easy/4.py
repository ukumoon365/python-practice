# 잔액 부족 알림
"""
1. 가격과 잔액을 입력
2. 가격과 잔액을 비교
3. 결과 출력
"""
price = int(input())
balance = int(input())

# 잔액보다 가격이 크면 "잔액이 부족합니다" 출력
if price > balance:
    print("잔액이 부족합니다")