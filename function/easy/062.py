# docstring 작성하고 __doc__ 로 읽기
# 1. 두 정수의 합을 반환하는 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 docsting 출력 / 결과 출력

def add(num1, num2: int) -> int:
    """두 정수의 합을 반환한다."""
    return num1 + num2

# 정수 입력
parts = input().split()
a = int(parts[0])
b = int(parts[1])

# 함수 호출 및 docsting 출력 / 결과 출력
print(add.__doc__)
print(add(a, b))