# 구간 합
# 1. 구간 합 함수 정의
# 2. 정수 입력 / 정수화 (컴프리헨션)
# 3. 함수 호출 및 출력

def range_sum(n: int, start: int = 1) -> int:
    """
    구간 합 함수
    
    Args:
        n (int): 끝값
        start (int): 시작값 (기본 1)

    Returns:
        int: start부터 n까지의 구간의 총합값
    """

    return sum(range(start, n + 1))

# 정수 입력
parts = input().split()
    
# parts 정수화
values = [int(value) for value in parts]

# 결과 출력
if len(values) == 1:
    print(range_sum(values[0]))
else:
    print(range_sum(values[0], values[1]))