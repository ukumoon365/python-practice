# global 키워드로 상태 바꾸기
# 1. 전역 변수 값 바꾸는 함수 정의
# 2. 문자열 입력
# 3. 리스트 순회 및 함수 호출
# 4. 결과 출력

def set_status(new: str) -> None:
    """
    전역 변수 status 값을 바꾸는 함수
    
    Global:
        status (str): 입력 받은 값으로 값을 바꿀 전역 변수
    
    Args:
        new (str): 바꿀 값

    Returns:
        None
    """
    global status

    status = new

# 문자열 기본 값
status = "대기"

# 문자열 입력
commands = input().split()

# 리스트 순회
for new in commands:
    set_status(new)

# 결과 출력
print(status)