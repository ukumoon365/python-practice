# docstring 가진 제곱 함수
# 1. 정수를 제곱하는 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력

def square(n: int) -> int:
    """
    정수의 제곱을 반환 함수

    Args:
        n (int): 정수
    
    Returns:
        int: 정수 제곱값
    """
    return n * n 

# 정수 입력
n = int(input())


# 결과 출력
print(square.__doc__)
print(square(n))