# 매개변수와 전역변수 함께쓰기
# 1. 세율 계산 함수 정의 
# 2. 정보 입력
# 3. 함수 호출 및 출력

# 세율 계산 함수 정의
def apply(price: int) -> int:
    """
    세율 계산 함수

    Globals:
        rate (int): 세율
        
    Args:
        price (int): 가격

    Returns:
        int: 세율 계산 결과값
    """
    return price + price * rate // 100

# 정보 입력
parts = input().split()
price0 = int(parts[0])
rate = int(parts[1])

# 반환값 출력
print(apply(price0))