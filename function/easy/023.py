# 시그니처 읽기
# 1. 주소 생성 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def connect(host: str, *, port: int) -> str:
    """
    주소 생성 함수

    Args:
        host (str): 호스트 값
        port (int): 포트 값

    Returns:
        str: 주소 값
    """
    return host + ":" + port

# 정보 입력
parts = input().split()
host = parts[0]
port = parts[1]

# 함수 호출 및 결과 출력
print(connect(host,port=port))