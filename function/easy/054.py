# 부호 판별 함수
# 1. 부호 판별 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력

# 부호 판별 함수 sign() 정의
def sign(n: int) -> int:
    """
    부호 판별 함수

    Args:
        n (int): 입력 받을 정수

    Returns:
        str:양수이면 "양수" / 음수이면 "음수" / 0이면 "0"  
    """
    
    if n > 0:
        return "양수"
    elif n < 0:
        return "음수"
    else:
        return 0

# 정수 입력
n = int(input())

# 결과 출력
print(sign(n))
