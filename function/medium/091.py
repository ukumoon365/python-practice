# 절댓값과 부호
# 1. 절댓값, 부호 반환 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def abs_sign(n: int)-> tuple[int, str]:
    """
    절댓값, 부호 반환 함수
    
    Args:
        n (int): 입력 받은 정수

    Returns:
        tuple[int, str]: 절댓값, "음수" | "양수" | "0"
    """

    sign = "음수" if n < 0 else "양수" if n > 0 else "0"
    
    return abs(n), sign

# 정수 입력
n = int(input())

# 결과 출력
print(*abs_sign(n))