# 네 가지 통계 한 번에
# 1. 최솟값, 최댓값, 합, 평균 값 반환 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def stats4(nums: list[int]) -> tuple[int]:
    """
    최솟값, 최댓값, 합, 평균 값을 반환 하는 함수

    Args:
        nums (list[int]): 입력 받은 정수의 리스트

    Returns:
        tuple[int]: 최솟값, 최댓값, 합, 평균 
    """
    sum_nums = sum(nums)

    return min(nums), max(nums), sum_nums, sum_nums // len(nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(*stats4(nums))