# 키워드 인자로 프로필 만들기
# 1. 프로필 만들기 함수 정의
# 2. 정보 입력
# 3. 함소 호출 및 출력
def make_profile(name: str, age: str) -> str:
    """
    프로필 만들기 함수

    Args:
        name (str): 이름
        age (str): 나이
    
    Returns:
        age: 형태의 프로필 출력
    """
    return f"{name}({age})"

# 정보 입력
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 결과 출력
print(make_profile(**opts))
