# 문자열 반복
# 1. 문자열 반복 함수 정의
# 2. 문자열 입력
# 3. 함수 호출 및 출력
def repeat_text(text: str, times: int=2) -> str:
    """
    문자열 반복 함수

    Args:
        text (str): 문자열
        times (int): 반복 횟수 (기본 2)

    Returns:
        str: 반복된 문자열
    """
    return text * times

# 문자열 입력
parts = input().split()

# 결과 출력
if len(parts) == 1:
    print(repeat_text(parts[0]))
else:
    print(repeat_text(parts[0], int(parts[1])))