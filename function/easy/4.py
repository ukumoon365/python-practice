# 직사각형 넓이 계산 함수
"""
1. 직사각형 넓이 계산 함수 정의
2. 가로, 세로 값 입력
3. 함수 호출 및 출력
"""

def area(w: int, h: int) -> int:
    """
    직사각형 넓이 계산 함수
    
    Args:
        w (int): 가로 값
        h (int): 세로 값
    
    Returns:
        int: 넓이 계산 결과값
    """
    return w * h

w, h = [int(x) for x in input().split()]

# 결과 출력
print(area(w, h))