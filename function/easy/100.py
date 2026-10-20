# 총액 계산
# 1. 총액 계산 함수 정의
# 2. 단가 및 수량(생략 가능) 입력
# 3. 함수 호출 및 출력

def total_price(unit_price: int, count: int = 1) -> int:
    """
    총액 계산 함수

    Args:
    unit_price (int): 단가
    count (int): 수량 (기본 1)

    Returns:
    int: 총액 계산 결과값
    """

    return unit_price * count

# 단가 및 수량 입력
parts = input().split()

# 결과 출력
print(total_price(*map(int, parts)))