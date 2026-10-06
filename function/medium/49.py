# global 있을 때 vs 없을 때
# 1. global 있을 때, 없을 때 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력


# global를 사용하지 않고 전역변수 값을 바꾸는 함수 without_global() 정의
def without_global(v: int) -> None:
    """
    global를 사용하지 않고 징변수 값을 바꾸는 함수

    Args:
        x (int): v 값으로 바뀔 변수
        v (int): x 값을 바꿀 변수
    
    Returns:
        None
    """
    x = v

# global를 사용하고 전역변수 값을 바꾸는 함수 with_global() 정의
def with_global(v):
    """
    global를 사용하고 전역변수 값을 바꾸는 함수

    Global:
        x (int): v 값으로 바뀔 변수

    Args:
        v (int): x 값을 바꿀 변수

    Returns:
        None
    """
    global x

    x = v

# 정수 입력
parts = input().split()
x = int(parts[0])
a = int(parts[1])
b = int(parts[2])


# 함수 호출 및 출력
without_global(a)
print(x)

with_global(b)
print(x)
