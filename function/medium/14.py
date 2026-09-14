# 이벤트 로그
"""
1. 이벤트 로그 함수 정의
2. 이벤트 정보 입력
3. 함수 호출 및 출력
"""

# 이벤트 로그 함수 정의
def log_event(event: str, *details: str, level: str = "INFO") -> str:
    """
    이벤트 로그 함수 

    Args:
        event (str): 이벤트 이름
        *details (str): 임의 개수의 상세정보
        level (str): 로그 레벨 (기본값 "INFO")
    
    Returns:
        str: 이벤트 로그 문자열
    """
    return f"{level}: {event} ({len(details)})"

# 이벤트 정보 입력
raw = input().split()
pos = [t for t in raw if "=" not in t]
event = pos[0]
details = pos[1:]
level = "INFO"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "level":
            level = v

# 결과 출력
print(log_event(event, *details, level=level))