# 거듭제곱
# 1. 거듭 제곱 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력
def power(base: int, exp: int= 2) -> int:
    """
    거듭 제곱 함수

    Args:
        base (int): 제곱할 값
        exp (int): 지수

    Returns:
        int: 제곱값 
    """
    return base ** exp

# 정수 입력 (정수와 지수는 공백으로 구분)
parts = input().split()

# 문자열 리스트 정수화 (정수와 지수 토큰으로 구별)
values = [int(num) for num in parts]

# 결과 출력
if len(values) == 1:
    print(power(values[0]))
else:
    print(power(values[0], values[1]))