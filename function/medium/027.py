# 시그니처 읽기
# 1. 값들을 잇는 함수 정의
# 2. 정보 입력
# 3. 결과 출력

def join_all(*values: str, sep: str) -> str:
    """
    값들을 잇는 함수
    
    Args:
        *values (str): 임의 개수의 문자값
        sep (str): 연결자
    
    Returns:
        str: 연결자로 이어진 문자열
    """
    return sep.join(values)

# 정보 입력
parts = input().split()
values = parts[:-1]
sep = parts[-1]

# 함수 호출 및 결과 출력
print(join_all(*values, sep=sep))