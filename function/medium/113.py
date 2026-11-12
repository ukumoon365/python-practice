# 가변 인자 모두 곱하기
# 1. 가변 인자 총 곱셈 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def product_all(*nums: int) -> int:
    """
    가변 인자들을 모두 곱한 값을 반환 하는 함수

    Args:
        nums (int): 임의 개수의 정수들
    
    Returns:
        int: 가변 인자들을 모두 곱한 값
    """
    result = 1
    for n in nums:
        result *= n

    return result

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(product_all(*nums))