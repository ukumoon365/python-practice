# 안전한 나눗셈
# 1. 안전한 나눗셈 함수 정의
# 2. 두 정수 입력
# 3. 함수 호출 및 출력
def safe_divide(a: int, b: int) -> int | str:
    """
    안전한 나눗셈 함수

    Args:
        a, b (int): 입력 받은 두 정수
    

    Returns:
        str: if b == 0 -> "오류"
        int: 나눗셈 결과 값 
    """
    if b == 0:
        return "오류"
    
    return a // b

# 두 정수 입력
a, b = [int(x) for x in input().split()]

# 결과 출력
print(safe_divide(a, b))
