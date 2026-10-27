# 키워드 인자로 넓이 계산
# 1. 넓이 계산 함수 정의
# 2. 가로, 세로값 입력
# 3. 함수 호출 및 출력
def rectangle_kw(width: int, height: int) -> int:
    """
    키워드 인자로 넓이 계산 및 반환 함수

    Args:
        width (int): 가로 길이
        height (int): 세로 길이

    Returns:
        int: 넓이 계산값
    """
    return width * height

# 가로, 세로값 입력
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 함수 호출 및 결과 출력
print(rectangle_kw(**opts))
