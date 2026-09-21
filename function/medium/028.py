# 시그니처 읽기
# 1. 합계 보고 함수
# 2. 정보 입력
# 3. 함수 호출 및 결과 출력

def report(title: str, *values: int, unit: str) -> str:
    """
    합계 보고 함수
    
    Args:
        title (str): 제목
        *values (int): 임의 개수의 값
        unit (str): unit 값

    Returns:
        str: 합계 보고 결과
    """
    s = 0 # 합계 저장 변수

    # 합계 계산 for문
    for v in values:
        s += v
    
    return title + ": " + str(s) + unit

# 정보 입력
parts = input().split()
title = parts[0]
values = [int(x) for x in parts[1:-1]]
unit = parts[-1]

# 함수 호출 및 결과 출력
print(report(title, *values, unit=unit))