# 시그니처 읽기
# 1. 거듭제곱 함수 정의
# 2. 값 입력
# 3. 함수 호출 및 출력 

def power(base: int, *, exp: int) -> int:
    """
    거듭 제곱 함수
    
    Args:
        base (int): 밑
        exp (int): 지수

    Return:
        int: 거듭 제곱 계산 값
    """
    return base ** exp

# 계산 값 입력
parts = input().split()
base = int(parts[0])
exp = int(parts[1])

# 결과 출력
print(power(base, exp=exp))