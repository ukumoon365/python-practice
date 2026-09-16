# 두 수의 차
# 1. 두 수의 차 계산 함수 정의
# 2. 정수 2개 입력
# 3. 함수 호출 및 결과 출력

def difference(first_num: int, second_num: int) -> int:
    """
    두 수의 차 계산 

    Args:
        first_num, second_num (str): 두 정수
    
    Returns:
        int: 두 수의 차 계산값
    """
    return first_num - second_num

# 두 정수 입력
a, b = [int(x) for x in input().split()]

# 결과 출력
print(difference(a, b))
