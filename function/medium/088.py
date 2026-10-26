# 첫 음수 찾기
# 1. 음수 찾는 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def first_negative(nums: list[int]) -> int | str:
    """
    처음 나오는 음수를 찾는 즉시 반환 함수

    Args:
        nums (list[int]): 입력 받은 정수의 리스트

    Returns:
        int | str: 음수 | 없음
    """
    for num in nums:
        if num < 0:
            return num
    
    return "없음"

# 정수 입력
nums = [int(x) for x in input().split()]

# 함수 호출 및 출력
print(first_negative(nums))
