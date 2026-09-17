# 두 수의 곱 함수
"""
1. 두 수의 곱 함수 정의
2. 두 수 입력
3. 함수 호출 및 출력
"""
def multiply(a: int, b: int) -> int:
    """
    두 수의 곱 함수

    Args:
        a (int): 첫 번째 정수
        b (int): 두 번째 정수

    Returns:
        int: 두 수의 곱
    """
    return a * b
 
# 두 수 입력
a, b = [int(x) for x in input().split()]

# 결과 출력
print(multiply(a, b))