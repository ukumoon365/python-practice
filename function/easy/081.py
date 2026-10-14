# 둘레와 넓이
# 1. 둘레 넓이 반환 함수 정의
# 2. 가로, 세로 값 입력
# 3. 결과 출력

def rect(w, h: int) -> tuple[int, int]:
    """
    둘레와 넓이를 계산 후 반환하는 함수
    
    Args:
        w (int): 가로 길이
        h (int): 세로 길이

    Returns:
        tuple[int, int]: 둘레, 넓이 다중 반환
    """
    return 2*(w+h), w*h

# 가로, 세로값 입력
w, h = [int(x) for x in input().split()]

# 결과 출력
print(*rect(w, h))