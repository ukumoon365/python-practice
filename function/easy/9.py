# 정사각형 넓이 함수
"""
1. 정사각형 넓이 계산 함수 정의
2. 한변의 길이 입력
3. 함수 호출 및 출력
"""
def square_area(s: int) -> int:
    """
    정사각형 넓이 계산

    Args:
        s (int): 한변의 길이
    
    Returns:
        int: 정사각형의 넓이
    """
    return s * s

s = int(input())

# 결과 출력
print(square_area(s))