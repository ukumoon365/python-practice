# 제목 태그 만들기
# 1. 제목 태크 만들기 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def build_tag(name: str, level: int = 1) -> str:
    """
    제목 태그 만들기 함수

    Args:
        name (str): 제목
        level (int): 태그 개수 / 기본 1

    Returns:
        str: 태그값과 제목 반환
    """
    return "#" * level + name

# 정보 입력
parts = input().split()

# 결과 출력
if len(parts) == 1:
    print(build_tag(parts[0]))
else:
    print(build_tag(parts[0], int(parts[1])))