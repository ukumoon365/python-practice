# 허용 메뉴 검사
# 1. 주문을 입력
# 2. 주문 내용이 메뉴에 있는 메뉴인지 확인
#    있다면 -> 주문 가능
#    없다면 -> 주문 불가
# 3. 결과 출력

# 메뉴 tuple
menu = ("Espresso", "Latte", "Cappuccino", "Americano")

# 주문 입력
order = input()

# 주문 가능 여부 판별 if문 및 결과 출력
if order in menu:
    print("주문 가능")
else:
    print("주문 불가")