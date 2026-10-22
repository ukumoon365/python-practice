# 받은 인자 개수 세기
# 1. 받은 인자 개수 세는 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력

def count_args(*nums: list[int]) -> int:
    """
    입력 받은 인자값 개수 카운트 함수

    Args:
        nums (list[int]): 입력 받은 인자값들

    Returns:
        int: 인자값의 개수
    """
    return len(nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 함수 호출 및 출력
print(count_args(*nums))
