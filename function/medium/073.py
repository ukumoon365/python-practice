# 초를 분,초 문자열로
# 1. 초를 분, 초 문자열로 변환하는 함수 정의
# 2. 초 입력
# 3. 함수 호출 및 결과 출력
def sec_to_str(sec: (int)) -> str:
    """
    초를 분, 초 문자열로 변환하는 함수

    Args:
        sec (int): 입력 받은 초

    Returns:
        str: f"{change_min}분 {change_sec}초"
    """
    change_min = sec // 60  # 분 변환
    change_sec = sec % 60   # 초 벼

    return f"{change_min}분 {change_sec}초"

# 초 입력
sec = int(input())

# 결과 출력
print(sec_to_str(sec))
