# 리스트를 풀어 함수에 넘기기 
# 1. 세 정수를 더하는 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def add3(a, b, c: int) -> int:
    """
    세 정수를 더하느 함수

    Args:
        a, b, c (int): 정수

    Returns:
        int: 세 정수의 합
    """
    return a + b + c

# 정수 입력
nums = [int(x) for x in input().split()]

# 함수 호출 및 출력 
print(add3(*nums))