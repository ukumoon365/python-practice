# 짝수 판별 함수
# 1. 짝수 판별 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력

# 짝수 판별 함수 정의
def is_even(n: int) -> bool:
    """
    짝수 판별 함수

    Args:
        n (int): 입력 받은 정수

    Returns:
        bool: 짝수 판별 결과값
    """
    return n % 2 == 0

# 정수 입력
n = int(input())

# 함수 호출 및 결과 출력
print(is_even(n))