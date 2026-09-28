# 시그니처 읽기
# 1. API 호출 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력 

# API 호출 함수
def api(endpoint: str, *args: str, method: str ="GET", **other: str) -> str:
    """
    API 호출

    Args:
        endpoint (str): 엔드 포인트
        *args (str): 임의 개수의 옵션값
        method (str): 기본 값 GET
        **other (str): 임의 개수의 옵션값
    """
    return endpoint + " " + method + " a" + str(len(args)) + " h" + str(len(other))

# 정보 입력
raw = input().split()
pos = [t for t in raw if "=" not in t]
endpoint = pos[0]
args = pos[1:]
method = "GET"
headers = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "method":
            method = v
        else:
            headers[k] = v

# api 함수 호출 및 결과 출력
print(api(endpoint, *args, method=method, **headers))