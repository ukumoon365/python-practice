# 주문 처리
# 1. 주문 방식, 가격 입력
# 2. 입력값에 따라 주문 방식 판별 
# 3. 결과 출력

# 주문 방식, 가격 입력
order_type = input()
price = 15000

# 주문방식(배달,포장) 확인
if order_type == "배달":
    # 거리 입력
    distance = int(input())

    # 배달 거리에 따른 배달비 계산
    delivery_price = 3500 if distance > 3 else 2000

    # 총액 계산
    total_price = price + delivery_price

    # 결과 출력
    print(f"배달 주문: 음식 {price}원 + 배달비 {delivery_price}원 = 총 {total_price}원")

elif order_type == "포장":
    discount = 2000  # 할인 2000원

    # 총액 계산
    total_price = price - discount

    # 결과 출력
    print(f"포장 주문: 음식 {price}원 - 할인 {discount}원 = 총 {total_price}원")
else:  # 그 외 
    print("잘못된 주문 방식입니다.")