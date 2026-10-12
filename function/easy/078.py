# 몫과 나머지
# 1. 몫과 나머지(다중 반환) 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 결과 출력

def divide(a, b: int) -> int:
    """
    몫과 나머지 반환 함수

    Args:
        a (int): 나뉠 정수
        b (int): 나눌 정수

    Returns:
        int: 몫
        int: 나머지
    """

    return a // b, a % b

# 정수 입력
a, b = [int(x) for x in input().split()]

# 결과 출력
print(*divide(a, b))