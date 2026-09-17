# 1부터 n까지 합 함수
"""
1. 1부터 n까지 더하는 함수 정의
2. n값 입력
3. 함수 호출 및 출력
"""

def sum_to(n: int) -> int:
    """
    1부터 n까지의 합 함수

    Args:
        n (int): 1 이상의 정수

    Returns:
        result (int): 1부터 n까지의 합
    """
    # 결과값 초기화
    result = 0

    for num in range(1, n + 1):
        result += num

    return result

# n값 입력
n = int(input())

# 결과 출력
print(sum_to(n))