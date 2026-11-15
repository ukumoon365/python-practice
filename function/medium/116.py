# 가변 인자의 범위
# 1. 가변 인자의 범위 반환 함수 정의
# 2. 정수 입력
# 3. 결과 출력
def range_span(*nums: int) -> int:
    """
    가변 인자의 범위 (최대 - 최소)깂을 반환하는 함수
    Args:
        *nums (int): 임의 개수 정수들

    Returns:
        int: 인자 값의 최댓값 - 최솟값의 값을 반환
    """
    return max(nums) - min(nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(range_span(*nums))
