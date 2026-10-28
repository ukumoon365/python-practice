# 메뉴와 사이드
# 1. 메뉴, 사이드 주문 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def menu(name: str, *sides: str) -> str:
    """
    메뉴와 사이드 주문 함수

    Args:
        name (str): 메뉴
        *sides (str): 임의 개수의 추가 메뉴

    Returns:
        str: 메뉴와 추가메뉴 반환
    """
    return f"{name} ({','.join(sides)})" if sides else name

# 정보 입력
raw = input().split()
name = raw[0]
sides = raw[1:]

# 함수 호출 및 출력
print(menu(name, *sides))
