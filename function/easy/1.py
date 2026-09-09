# 인사말 출력 함수
"""
1. 인사말 출력 함수 정의
2. 이름 입력
3. 함수 호출 및 출력
"""

# 인사말 함수 정의
def greet(name: str) -> str:
    """
    # 인사말 문자열 반환 함수
    Args:
        name (str): 이름

    Returns:
        str: 인사말 반환 
    """
    return (f"안녕하세요, {name}님!")

# 이름 입력 
name = input()

# 인사말 출력
print(greet(name))