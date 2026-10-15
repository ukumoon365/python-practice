# 기본 인사말
# 1. 인사말 반환 함수 정의
# 2. 이름과 인사말 입력
# 3. 인사말 입력 유무 판별
#   1) 함수 호출 및 출력
def greet(name: str, greeting="안녕하세요") -> str:
    """
    인사말을 반환하는 함수
    
    Args:
        name (str): 이름
        greeting (str): 인사말 (기본값: 안녕하세요)

    Returns:
        str: 인사말
    """
    return f"{greeting}, {name}님!"

# 이름과 인사말 입력
parts = input().split()

# 인사말 입력 유무 판별 if문
if len(parts) == 1: # 이름만 입력된 경우
    print(greet(parts[0]))
else:
    print(greet(parts[0], parts[1]))