# 최종 결제 금액
# 1. 결제 금액 계산 함수 정의
# 2. 금액과 할인액 입력
# 3. 결과 출력
def final_price(price: int, discount=0) -> int:
    """
    최종 결제 금액 계산 함수

    Args:
        price (int): 가격
        discount (int): 할인액 (기본 0)

    Returns:
        int: 최종 결제 금액
    """
    return price - discount
# 금액 입력 (금액과 할인액 공백 구분)
parts = input().split()

# parts 리스트 정수화 (금액과 할인액 토큰 구분)
values = [int(value) for value in parts]

# 결과 출력
if len(values) == 1:
    print(final_price(values[0]))
else:
    print(final_price(values[0], values[1]))