# 최소, 최대, 합
# 1. 최소, 최대, 합 반환 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def stats(nums: list[int]) -> tuple[int]:
    """
    최솟값, 최댓값, 합 반환 함수

    Args:
        nums (list[int]): 입력 받은 정수의 리스트

    Returns:
        tuple[int]: 최솟값, 최댓값, 합
    """
    return min(nums), max(nums), sum(nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(*stats(nums))