# docstring 가진 최댓값 함수
# 1. 두 정수 비교 후 큰 수 반환 함수 정의
# 2. 두 정수 입력
# 3. 함수 호출 및 출력

def max_two(a: int, b: int) -> int:
    """
    두 수 중 큰 값을 반환 함수

    Args:
        a, b (int): 두 정수
    
    Returns:
        int: 더 큰 수
    """
    if a > b:
        return a
    return b

# 두 정수 입력
parts = input().split()
a = int(parts[0])
b = int(parts[1])

# 함수 호출 및 출력
print(max_two.__doc__)
print(max_two(a, b))