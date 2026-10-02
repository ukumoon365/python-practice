# global 키워드로 잔액 관리
# 1. 전역 변수에 증감액을 받아 계산하는 함수 정의
# 2. 정보 입력
# 3. 증감액 리스트 순회
# 4. 결과 출력

def apply(price: int) -> None:
    """
    전역 변수 balance에 증감액을 받아 계산하는 함수
    
    Globals:
        balance (int): 증감액을 받아 계산되는 전역 변수

    Args:
        price (int): 입력 받을 증감액
    
    Returns:
        None
    """

    global balance 

    balance += price

# 정보 입력
parts = input().split()
balance = int(parts[0])
changes = [int(x) for x in parts[1:]]


# 증감액 리스트 순회
for price in changes:
    apply(price)

# 결과 출력
print(balance)
