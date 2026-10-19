# 회문 판별 함수
# 1. 회문 판별 함수 정의
# 2. 문자열 입력
# 3. 함수 호출 및 출력

def is_palindrome(s: str) -> bool:
    """
    회문 판별 함수

    Args:
        s (str): 입력 받은 문자열

    Returns:
        bool: 회문이면 Ture, 아니면 False
    """

    return s == s[::-1]

# 문자열 입력
s = input()

# 결과 출력
print(is_palindrome(s))