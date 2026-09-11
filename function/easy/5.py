# 절댓값 직접 만들기
"""
1. 정수를 절댓값으로 바꾸는 함수 정의
2. 정수 입력
3. 함수 호출 및 출력
"""
def my_abs(n: int) -> int:
    """
    절댓값 만드는 함수

    Args:
        n (int): 정수
    
    Returns:
        int: 절댓값 n
    """
    if n < 0:
        return -n
    else:
        return n

# 정수 입력
n = int(input())

# 함수 호출 및 결과 출력
print(my_abs(n))