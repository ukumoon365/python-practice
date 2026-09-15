# 구분자로 잇기
"""
1. 구분자로 문자 연결하는 함수 정의
2. 연결할 문자와 구분자 입력(선택)
3. 함수 호출 및 출력
"""
def make_list(first: str, *rest: str, sep: str="-") -> str:
    """
    구분자로 문자 연결
    
    Args:
        first (str): 시작 문자
        *rest (str): 임의 개수의 문자
        sep (str): 구분자 / 기본값 "-" 
    """
    return sep.join([first] + list(rest))

# 문자 및 구분자 입력
raw = input().split()
pos = [t for t in raw if "=" not in t]
first = pos[0]
rest = pos[1:]
sep = "-"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "sep":
            sep = v

# 결과 출력
print(make_list(first, *rest, sep=sep))
