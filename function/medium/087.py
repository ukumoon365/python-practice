# 점수 검증
# 1. 점수 검증 함수 정의
# 2. 점수 입력
# 3. 함수 호출 및 출력
def evaluate(score: int) -> str:
    """
    정수 점수 검증 함수

    Args:
        score (int): 입력 받은 점수

    Returns:
        str: 검증 결과값 
    """ 
     
    if score < 0 or score > 100: 
        return "유효하지 않음"
    elif score >= 60: 
        return "합격"
    else: 
        return "불합격"

# 점수 입력
score = int(input())

# 결과 출력
print(evaluate(score))