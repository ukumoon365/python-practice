# 합과 평균
# 1. 합과 평균 함수 정의
# 2. 정수 입력 (공백 구분)
# 3. 함수 호출 및 출력
def sum_avg(nums: list[int]) -> tuple[int, int]:
    """
    합과 평균(정수 나눗셈, 소수점 이하 버림) 값 반환 함수

    Args:
        nums(list[int]): 입력 받은 정수 리스트

    Returns:
        tuple[int, int]: 합, 평균(소수점 이하 버림)
    """
    # 총합 
    sum_nums = sum(nums)

    return sum_nums, sum_nums // len(nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(*sum_avg(nums))