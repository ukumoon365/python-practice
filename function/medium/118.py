# 첫 인자와 마지막 인자의 합
# 1. 첫 인자와 마지막 인자의 합 계산 함수 정의
# 2. 인자값 입력
# 3. 함수 호출 및 출력
def first_and_last_sum(*nums: int) -> int:
    """
    첫 인자와 마지막 인자값의 합을 반환하는 함수

    Args:
        *nums (int): 임의 개수의 정수들
    
    Returns:
        int: 첫 인자값과 마지막 인자값의 합
    """

    return nums[0] + nums[-1]

# 인자값 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(first_and_last_sum(*nums))