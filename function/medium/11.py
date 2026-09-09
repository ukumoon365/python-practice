# 합계 보고
"""
1. 합계 보고 함수 정의
2. 제목, 값, 단위(선택) 입력
3. 함수 호출 및 출력
"""

# 합계 보고 함수 정의
def report(title: str, *values: int, unit: str = "개"):
    """ 
    합계 보고 함수
    
    Args:
        title (str): 제목
        *values (int): 임의 개수의 값
        nuit (str): 단위 / 기본 "개"
    
    Returns:
        str: 제목, 값들의 총합, 단위 

    """
    return f"{title}: {sum(values)}{unit}"

raw = input().split()   # 제목, 값 입력 / 공백 구분
pos = [t for t in raw if "=" not in t]  # =가 들어가지 않은 값들만 리스트 추가
title = pos[0]  # 제목 / 제일 처음 입력 된 값 
values = [int(x) for x in pos[1:]]  # 제목을 제외한 값 리스트
unit = "개" # 단위 기본값 초기화

for t in raw:
    if "=" in t:    # "="이 포함된 문자
        k, v = t.split("=", 1)  # "="를 기준으로 값 나누기
        if k == "unit": 
            unit = v    # 단위 값 변경

# 함수 호출 및 출력
print(report(title, *values, unit=unit))
