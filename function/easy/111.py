# 가변 인자 중 최솟값
# 1. 가변 인자값 중 최솟값 반환 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력

def min_all(*args: list[int]) -> int:
    """
    가변 인자 값 중 최솟값 반환 함수

    Args:
        args (list[int]): 임의 개수의 정수

    Returns:
        int: 가변 인자 값 중 최솟값
    """
    return min(args)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(min_all(*nums))
