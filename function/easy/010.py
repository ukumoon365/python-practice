# 세제곱 함수
"""
1. 세제곱 함수 정의
2. 정수 한개 입력
3. 함수 호출 및 출력
"""
def cude(n: int) -> int:
    """
    세제곱 함수
    
    Args:
        n (int): 한개의 정수

    Returns:
        int: n의 세제곱 결과값
    """
    return n * n * n

# 정수 입력
n = int(input())

# 결과 출력
print(cude(n))