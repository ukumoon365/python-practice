# 세 수의 합 함수
"""
1. 세 수의 합 함수 정의
2. 세 수 입력
3. 함수 호출 및 출력
"""


def sum_three(a: int, b: int , c: int) -> int:
    """
    세 수의 합 함수

    Args:
        a, b, c (int): 3개의 정수

    Returns:
        int: 세 수의 합 
    """
    
    return a + b + c

# 세 수 입력
a, b, c = [int(x) for x in input().split()]

# 결과 출력
print(sum_three(a, b, c))
        