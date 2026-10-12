# 정수 평균
# 1. 정수들의 평균을 계산하는 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def average(nums: list[int]) -> int:
    """
    정수들의 평균을 계산하는 함수
    
    Args:
        nums (list[int]): 입력 받은 정수들의 리스트

    Returns:
        int: 평균 계산 후 소수점 이하는 버림
    """

    return sum(nums) // len(nums)
# 정수 입력 및 리스트화
nums = [int(x) for x in input().split()]

# 함수 호출 및 출력
print(average(nums))