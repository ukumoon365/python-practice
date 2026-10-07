# 점수 등급 함수
# 1. 입력 받은 점수를 등급으로 구별하는 함수 정의
# 2. 점수 입력
# 3. 함수 호출 및 출력

def grade(score: int) -> str:
    """
    입력 받은 점수를 등급으로 구별하는 함수

    Args:
        score (int): 입력 받은 점수

    Return:
        str: 90 이상 "A" / 80 이상 "B" / 70 이상 "C" / 70 미만 "F"
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# 점수 입력 
score = int(input())

# 결과 출력
print(grade(score))
