# 범위 제한 clamp
# 1. 범위 제한 값 반환 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def clamp(value: int, low: int = 0, high: int = 100) -> int:
    """
    해당 범위의 제한 값 반환 함수

    Args:
        value (int): 값
        low (int): 하한 / 기본 0
        high (int): 상항 / 기본 100

    Returns:
        int: 해당 범위에 맞는 제한 값 반환
    """
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value

# 정보 입력
parts = input().split()

# parts 정수화
values = [int(value) for value in parts]

# 결과 출력
if len(values) == 1:
    print(clamp(values[0]))
elif len(values) == 2:
    print(clamp(values[0], values[1]))
else:
    print(clamp(values[0], values[1], values[2]))
