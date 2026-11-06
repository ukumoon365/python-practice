# 옵션별 결제 금액
# 1. 옵션별 결제 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def price_with_options(base: int, tax: int = 10, ship: int = 0) -> int:
    """
    옵션별 결제 금액 계산 함수

    Args:
        base (int): 기본 가격
        tax (int): 세율(%) / 기본 10
        ship (int): 배송비 / 기본 0

    Returns:
        int: 옵션별 결제 금액 반환
    """
    return base + base * tax // 100 + ship


# 정보 입력
parts = input().split()

# parts 정수화
values = [int(value) for value in parts]

# 결과 출력
if len(values) == 1:
    print(price_with_options(values[0]))
elif len(values) == 2:
    print(price_with_options(values[0], values[1]))
else:
    print(price_with_options(values[0], values[1], values[2]))