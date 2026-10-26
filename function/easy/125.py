# 키워드 인자 개수 세기
# 1. 키워드 인자 카운트 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def count_kwargs(**kwargs: dict) -> int:
    """
    키워드 인자 개수 카운트 및 반환 함수

    Args:
        **kwargs (dict{str: int}): 임의 개수의 키워드 인자들
    Returns:
        int: 키워드 인자 개수 
    """
    return len(kwargs)

# 정보 입력
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 함수 호출 및 출력
print(count_kwargs(**opts))
