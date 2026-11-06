# 가변 인자 평균
# 1. 가변 인자 평균 계산 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def average_args(*nums: int) -> int:
    """
    가변 인자 평균값 반환 함수
    
    Args:
        nums (int): 임의 개수의 정수

    Returns:
        int: 가변 인자값의 평균값 반환
    """
    return sum(nums) // len(nums)
# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(average_args(*nums))
