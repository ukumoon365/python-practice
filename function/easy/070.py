# 리스트 합계 함수
# 1. 리스트 원소 합계 계산 함수 정의
# 2. 정수 입력 및 리스트화
# 3. 결과 출력

def list_sum(nums: list[int]) -> int:
    """
    리스트 원소들의 합계 계산 함수

    Args:
        nums (list[int]): 공백으로 구분된 정수들의 리스트

    Returns:
        int:리스트 원소들의 합계 
    """
    return sum(nums)

# 정수 입력 및 리스트화
nums = [int(x) for x in input().split()]

# 결과 출력
print(list_sum(nums))