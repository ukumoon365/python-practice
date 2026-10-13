# 최솟값과 최댓값
# 1. 최솟값, 최대값 반환 함수 정의
# 2. 정수 입력 및 리스트화
# 3. 결과 출력

def min_max(nums: list[int]) -> int:
    """
    입력 받은 숫자들 중 최솟값, 최댓값 반환 함수

    Args:
        nums (list[int]):입력 받은 숫자들의 리스트
    
    Returns: 
        int: min, max
    """
    return min(nums), max(nums)

# 정수 입력 및 리스트화
nums = [int(x) for x in input().split()]

# 결과 출력
print(*min_max(nums))