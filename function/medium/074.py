# 팩토리얼 함수
# 1. 팩토리얼 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def factorial(n: int) -> int:
    """
    팩토리얼 함수
    
    Args:
        n (int): 입력 받은 0이상의 정수

    Returns:
        result (int): 1 ~ n까지의 팩토리얼 / 0! = 1 
    """
    result = 1  # 팩토리얼 계산 결과 값
    
    for x in range(1, n + 1):
            result *= x

    return result

# 정수 입력
n = int(input())

# 결과 출력
print(factorial(n))