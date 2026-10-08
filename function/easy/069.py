# 문자열 반복 함수
# 1. 문자열 반복 함수 정의
# 2. 문자열 및 정수 입력
# 3. 함수 호출 및 출력 

def repeat(s: str, n: int) -> str:
    """
    입력 받은 문자열을 입력 받은 횟수만큼 반복하여 반환하는 함수

    Args:
        s (str): 입력 받은 문자열
        n (int): 문자열을 반복할 횟수

    Returns:
        str: 정해진 횟수만큼 반복된 문자열
    """
    return s * n

# 문자열 및 정수 입력
s = input()
n = int(input())


# 결과 출력
print(repeat(s, n))