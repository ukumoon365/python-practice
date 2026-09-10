# 더 큰 값 비교 후 반환
"""
1. 2개의 정수 입력 / 공백 구분
2. 두 수의 크기를 비교하는 함수 정의
3. 함수 호출 및 출력
"""

a, b = [int(x) for x in input().split()]

def bigger(a: int , b: int) -> int:
    """
    더 큰 값 반환 함수
    Args:
        a (int), b (int)): 2개의 정수

    Returns:
        int: 값 비교 후 더 큰 값 
    """
    if a > b:
        return a
    else: 
        return b

# 결과 출력
print(bigger(a, b))