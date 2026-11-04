# 할인율 적용
# 1. 할인율 적용 함수 정의
# 2. 가격, 할인율 입력
# 3. 함수 호출 및 출력
def discount_price(price: int, rate: int = 10) -> int:
    """
    할인율 적용 계산 함수

    Args:
        price (int): 가격
        rate (int): 할인율 / 기본 10

    Returns:
        int: 할인율 계산 결과 값
    """
    # 할인 금액
    discount = price * rate // 100

    return price - discount

# 가격, 할인율 입력
parts = input().split()

# 결과 출력
print(discount_price(*map(int, parts)))