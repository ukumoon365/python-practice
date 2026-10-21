# 여러 수의 합
# 1. 전체 합 계산 함수 정의
# 2. 정수 입력 (공백 구분)
# 3. 함수 호출 및 출력
def total(*nums: int) -> int:
    """
    전체 합 계산 함수
    Args:
        *nums (int): 임의 개수의 정수

    Returns:
        int: 전체 합 계산
    """
    return sum(nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(total(*nums))
