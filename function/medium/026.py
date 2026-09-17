# 시그니처 읽기
# 1. 부분 문자열 반환 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 결과 출력

def slice_text(text: str, *, start: int, end: int) -> str:
    """
    부분 문자열 반환 함수

    Args:
        text (str): 문자열
        start (int): 시작점
        end (int): 끝점

    Returns:
        str: 부분 문자열
    """
    return text[start:end]

# 정보 입력
parts = input().split()
text = parts[0]
start = int(parts[1])
end = int(parts[2])

# 함수 호출 및 결과 출력
print(slice_text(text, start=start, end=end))
