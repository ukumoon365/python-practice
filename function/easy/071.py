# 양수 개수 세기 함수
# 1. 양수의 개수 반환 함수 정의
# 2. 정수 입력 및 리스트화
# 3. 함수 호출 및 출력

def count_positive(nums: list[int]) -> int:
    """
    리스트 원소 중 양수의 개수를 반환하는 함수
    
    Args:
        nums (list[int]): 입력 받은 정수들의 리스트
        count (int): 양수의 개수를 카운트하는 지역 변수

    Return:
        int: 양수의 개수를 카운트
    """
    count = 0

    for num in nums:
        if num > 0:
            count += 1
    
    return count

# 정수 입력 및 리스트화
nums = [int(x) for x in input().split()]

# 결과 출력
print(count_positive(nums))
