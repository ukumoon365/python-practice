# 초를 시, 분, 초로 
# 1. 입력 받은 초를 시,분,초 변환 및 반환 함수 정의
# 2. 초 입력
# 3. 함수 호출 및 출력
def to_hms(sec: int) -> tuple[int, int, int]:
    """
    초를 시, 분, 초로 변환 및 반환 함수
    
    Args:
        sec (int): 입력 받은 초

    Returns:
        tuple[int, int, int]: 시 분 초 
    """

    return sec // 3600, (sec % 3600) // 60, sec % 60

# 초 입력
sec = int(input())

# 결과 출력
print(*to_hms(sec))