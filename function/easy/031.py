# 함수에서 전역변수 읽기
# 1. 메세지 입력
# 2. 공지 메세지 반환 함수 정의
# 3. 함수 호출

# 메세지 입력
message = input()

def announce() -> str:
    """
    공지 메세지 반환 함수

    Globals:
        message (str): 메세지
    
    Returns:
        str: 공지 메세지
    """
    return f"[공지] {message}"

# 함수 호출 및 결과 출력
print(announce())