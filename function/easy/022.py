# 시그니처 읽기
# 1. 문자열 반복 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def repeat(text : str, *, times: int) -> str:
    """
    문자열 반복 함수

    Args:
        text (str): 문자열
        times (int): 반복 횟수
    
    Returns:
        str: 반복 문자열
    """
    return text * times

# 값 입력
parts = input().split()
text = parts[0]
times = int(parts[1])

# 결과 출력
print(repeat(text, times = times))