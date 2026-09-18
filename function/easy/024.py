# 시그니처 읽기
# 1. 제목 태그 함수 정의
# 2. 정보 입력
# 3. 결과 출력

def tag(name: str, *, level: int) -> str:
    """
    제목 태그 함수

    Args:
        name (str): 제목
        level (int):  #개수
    
    Returns:
        str: 제목 태그
    """
    return "#" * level + name

# 정보 입력
parts = input().split()
name = parts[0]
level = int(parts[1])

# 함수 호출 및 결과 출력
print(tag(name, level=level))
