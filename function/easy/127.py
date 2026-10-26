# 키워드 인자로 인사하기
# 1. 키워드 인자값으로 인사말 제작 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def greet_kw(greeting: str, name: str) -> str:
    """
    키워드 인자값으로 인사말 제작 및 반환 함수

    Args:
        greeting (str): 인사말
        name (str): 이름
    
    Returns:
        str: f"{greeting}, {name}!"로 반환
    """
    return f"{greeting}, {name}!"

# 정보 입력
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 함수 호출 및 출력
print(greet_kw(**opts))
