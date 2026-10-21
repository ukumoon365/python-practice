# 두 단어 잇기
# 1. 두 단어를 구분자로 잇는 함수 정의
# 2. 단어 입력
# 3. 함수 호출 및 출력
def join_two(a: str, b: str, sep: str = "-") -> str:
    """
    두 단어를 구분자로 잇는 함수

    Args:
        a (str): 첫번째 단어
        b (str): 두번째 단어
        sep (str): 구분자

    Returns:
        str: 구분자로 이어진 두 단어 
    """

    return a + sep + b

# 단어 입력
parts = input().split()

# 결과 출력
print(join_two(*parts))