# 값 증가
# 1. 값 증가 함수 정의
# 2. 정수, 증가폭(생략 가능) 입력
# 3. 함수 호출 및 출력

def increment(n: int, step: int = 1) -> int:
    """
    값 증가 함수

    Args:
        n (int): 값
        step (int): 증가폭 (기본 1)

    Returns:
        int: 증가 폭에 따른 증가 값 
    """

    return n + step

# 정수 및 증가폭 입력
parts = input().split()

# parts 정수화
values = [int(value) for value in parts]

# 결과 출력
if len(values) == 1:
    print(increment(values[0]))
else:
    print(increment(values[0], values[1]))