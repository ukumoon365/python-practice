# 임의의 설정 키워드를 받아 정보를 출력
"""
1. 임의의 설정 키워드를 받아 형식에 맞는 문자열을 반환하는 함수 정의
2. 이름과 임의의 설정 키워드 입력
3. 함수 호출 및 출력
"""

def config(name: str, **settings: str) -> str:
    """ 
    설정 값 리턴
        
    Args:
        name (str): 이름
        **settings (str): 임의의 설정값들

    Returns:
        str: 입력 받은 데이터를 형식에 맞게 문자열로 반환
    """
    return f"{name} has {len(settings)} settings"

# 정보 입력
raw = input().split()
name = ""   # 이름 변수
settings = {}   # 설정값 변수

# 순회를 통해 이름과 설정값 구분
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        settings[k] = v
    else:
        name = t

# 결과 출력
print(config(name, **settings))