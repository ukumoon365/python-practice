# 문자열 뒤집기 함수
# 1. 문자열 뒤집기 함수 정의
# 2. 문자열 입력
# 3. 함수 호출 및 출력
def reverse(s: str) -> str:
    """
    문자열 뒤집기 함수

    Args:
    s (str): 입력 받은 문자열

    Returns:
    s[::-1] (str): 뒤집힌 문자열
    """

    return s[::-1]

# 문자열 입력
s = input()

# 함수 호출 및 출력
print(reverse(s))