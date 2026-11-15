# 가변 인자 중 양수만 합
# 1. 가변 인자 중 양수만 합계 및 반환 함수 정의
# 2. 정수 입력
# 3. 결과 출력 
def sum_positive(*nums: int) -> int:
    """
    가변 인자 중 양수만 합계 및 반환 함수
    
    Args:
        nums (int):임의 개수 정수들

    Returns:
        int: 양수만 합계 및 반환
    """
    return sum(n for n in nums if n > 0)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(sum_positive(*nums))
