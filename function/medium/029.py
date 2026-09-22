# 시그니처 읽기
# 1. 합계 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def merge(base: int, **extra: dict[str: int]) -> int:
    """
    합계 함수

    Args:
        base (int): 정수
        **extra (dict[srt: int]): 임의 개수의 문자와 정수의 딕셔너리

    Returns:
        int: 합계 계산값
    """
    total = base
    for k in extra:
        total += extra[k]
    return total

# 정보 입력
raw = input().split()
base = int(raw[0])
extra = {}
for t in raw[1:]:
    k, v = t.split("=")
    extra[k] = int(v)

# 함수 호출 및 결과 출력
print(merge(base, **extra))