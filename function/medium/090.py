# 첫 짝수 찾기
# 1. 처음 나오는 짝수 반환 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def first_even(nums: list[int]) -> int | None:
    """
    처음 나오는 짝수 반환 함수

    Args:
    nums (list[int]): 입력 받은 정수의 리스트 -> list

    Returns:
    int | None: 짝수 | 없음
    """
    for num in nums:
        if num % 2 == 0:
            return num
    # 없으면 None 

# 정수 입력
nums = [int(x) for x in input().split()]

# 함수 호출 및 출력
print(first_even(nums))