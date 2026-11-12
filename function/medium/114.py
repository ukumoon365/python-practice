# 가변 인자 중 짝수 개수
# 1. 가변 인자 중 짝수의 개수 카운트 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def count_even(*nums: int) -> int:
    """
    가변 인자 중 짝수의 개수 카운트 및 반환 함수
    Args:
        nums (int): 임의 개수의 정수

    Returns:
        int: 가변 인자 중 짝수 개수
    """
    # 짝수 카운트 변수
    even_count = 0

    for value in nums:
        if value % 2 == 0:
            even_count += 1

    return sum(n % 2 == 0 for n in nums)

# 정수 입력
nums = [int(x) for x in input().split()]

# 결과 출력
print(count_even(*nums))
