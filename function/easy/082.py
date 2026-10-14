# return 없는 함수의 결과
# 1. 인사말 출력 함수 정의
# 2. 이름 입력
# 3. 함수 호출 및 출력

def welcome(name: str) -> None:
    """
    name를 사용한 인사말 출력 함수
    
    Args:
        name (str): 이름

    Returns:
        None
    """
    print(f"{name}님 환영합니다")

# 이름 입력
name = input()

# 결과 출력
print(welcome(name))