# 분을 초로 변환
# 1. 분을 초로 변환하는 함수 정의
# 2. 분 입력
# 3. 함수 호출 및 결과 출력

def to_seconds(m: int) -> int:
    """
    분을 초로 변환 함수
    Args:
        m (int) = 분

    Returns
        int: 초로 변환한 값
    """

    return m * 60

# 분 입력
m = int(input())

# 함수 호출 및 결과 출력
print(to_seconds(m))