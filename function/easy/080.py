# 합과 곱
# 1. 두 수의 합, 곱의 결과 함수 정의
# 2. 두 정수 입력
# 3. 함수 호출 및 출력
def sum_product(a, b: int) -> int:
    """
    두 수의 합과 곱의 결과를 반환하는 함수

    Args:
        a, b (int): 입력 받은 두 수

    Returns:
        int: 두 수의 합, 두 수의 곱 결과값 튜플
    """
    return a + b, a * b

# 두 정수 입력
a, b = [int(x) for x in input().split()]

# 결과 출력 (언패킹)
print(*sum_product(a, b))