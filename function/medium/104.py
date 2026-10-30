# 합격 판정
# 1. 합격 판정 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력
def check_pass(score: int, pass_line: int = 60) -> str:
    """
    합격 판정 함수

    Args:
        score (int): 점수
        pass_line (int): 합격 커트라인 / 기본 60점

    Returns:
        str: 합격 판정 결과 반환
    """
    if score >= pass_line:
        return "합격"
    else:
        return "불합격"

# 정보 입력
parts = input().split()

# parts 정수화
values = [int(value) for value in parts]

# 결과 출력
if len(parts) ==1:
    print(check_pass(values[0]))
else:
    print(check_pass(values[0], values[1]))