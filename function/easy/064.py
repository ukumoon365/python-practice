# docstring 가진 인사 함수
# 1. 이름으로 인사말을 만들고 반환하는 함수 정의
# 2. 이름 입력
# 3. 함수 호출 및 출력

def greet(name: str) -> str:
    """
    이름으로 인사말을 만들고 반환 함수

    Args:
        name (str): 이름
    
    Returns:
        str: 인사말
    """
    return f"안녕하세요, {name}님!"

# 이름 입력
name = input()

# 결과 출력
print(greet.__doc__)
print(greet(name))