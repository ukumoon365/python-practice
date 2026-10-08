# 불변 객체(int)는 함수 안에서 바꿔도 원본 그대로
# 1. n + 1 값을 반환하는 함수 정의
# 2. 정수 입력
# 3. 결과 출력
def add_one(n: int) -> int:
    """
    n + 1 값을 반환하는 함수 정의
    
    Args:
        n (int): +1 계산을 할 정수

    Return:
        int: n + 1값
    """
    return n + 1

# 정수 입력
x = int(input())

# 결과 출력
print(add_one(x))
print(x) # 불변 객체(int)는 변함 없음