# 시그니처 읽기
# 1. 채움 문자열을 만드는 함수 정의
# 2. 값 입력
# 3. 함수 호출 및 결과 출력
def make_box(width: int, height: int, *, fill: str) -> str:
    """
    채움 문자열

    Args:
        width (int), height (int): 넓이 값
        fill (str): 채울 문자
    
    Returns:
        str: 채움 문자열
    """
    return fill * (width * height)

# 값 입력
parts = input().split()
width = int(parts[0])
height = int(parts[1])
fill = parts[2]


#함수 호출 및 결과 출력
print(make_box(width, height, fill=fill))