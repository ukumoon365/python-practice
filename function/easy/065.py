# 두 수가 같은가
# 1. 두 수 비교 함수 정의
# 2. 두 정수 입력
# 3. 함수 호출 및 출력

# 두 수가 같은지 비교하는 함수 정의
def is_equal(a: int, b: int) -> bool:
    """
    두 수가 같은지 비교하는 함수

    Args:
        a, b (int): 입력 받은 정수, 같은 값인지 비교 대상

    Retruns:
        bool: a == b 
    """
    return a == b

# 두 정수 입력
a, b = [int(x) for x in input().split()]

# 함수 호출 및 출력
print(is_equal(a, b))
