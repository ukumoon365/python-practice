# 두 수의 합 계산 
"""
1. 두 수의 합 계산 함수 정의
2. 두 개의 정수 입력
3. 함수 호출 및 출력
"""

# 두 수의 합 계산 함수 정의
def add(a: int, b: int) -> int:
    """
    두 수의 합 계산 함수
    
    Args:
        a (int): 첫번째 정수
        b (int): 두번째 정수 

    Returns:
        int: 두 수의 합
    """
    return a + b

# 두 개의 정수 입력 / 공백 구분
a, b = [int(x) for x in input().split()]

# 결과 출력
print(add(a, b))