# 시그니처 읽기
# 1. 채움 문자열 생성 함수 정의
# 2. 정보 입력
# 3. 결과 출력

def make_box(width: int, height: int, *, fill: str):
    """
    채움 문자열 생성

    Args:
        width, height (int): 가로, 세로 값
        fill (str): 채울 문자

    Returns:
        str: 채움 문자열
    """
    return fill * (width * height)

# 정보 입력
parts = input().split()
width = int(parts[0])
height = int(parts[1])
fill = parts[2]

# 함수 호출 및 결과 출력
print(make_box(width, height, fill=fill))