# 성과 이름 분리
# 1. 성과 이름 위치 변경 함수 정의
# 2. 이름 입력
# 3. 함수 호출 및 출력

def name_order(last: str, first: str) -> tuple[str, str]:
    """
    성과 이름을 위치 변환 함수

    Args:
        last (str): 성
        first (str): 이름

    Returns: 
        tuple[str, str]: 이름, 성
    """
    return first, last

# 이름 입력
last, first = input().split()

# 결과 출력
print(*name_order(last, first))