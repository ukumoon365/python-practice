# 세 수 중 최댓값
# 1. 세 수를 비교하여 가장 큰 값을 반환하는 함수 정의
# 2. 정수 3개 입력
# 3. 결과 출력

def max_three(a: int, b: int, c: int) -> int:
    """
    세 수를 비교하여 가장 큰 값을 반환하는 함수

    Args:
        a, b, c (int): 입력 받은 정수 / 비교 대상
    
    Returns:
        int: 가장 큰 값을 반환
    """
    return max(a, b, c) 

# 정수 3개 입력
a, b, c = [int(x) for x in input().split()]

# 결과 출력
print(max_three(a, b, c))
