# 딕셔너리를 풀어 함수에 넘기기
# 1. 인사말 반환 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def greet(greeting: str, name: str) -> str:
    """
    인사말 반환 함수
    
    Args:
        greeting (str): 인사말
        name (str): 이름

    Returns:
        str: 인사말
    """
    return greeting + ", " + name + "!"

# 정보 입력
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 함수 호출 및 출력
print(greet(**opts))