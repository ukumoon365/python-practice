# 조건에서 전역 변수 읽기
# 1. 매개변수, 전역변수 비교하는 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def in_stock(n:  int) -> str:
    """ 
    매개변수 n과 전역 stock를 비교하는 함수 
    
    Args
        n (int): 요청 수량

    Global 
        stock (int): 재고

    Return
        str: n <= stock 이면 "가능" 아니면 "불가" 
    """

    if n <= stock:
        return "가능"
    else:
        return "불가" 

# 정보 입력
parts = input().split()
n = int(parts[0])
stock = int(parts[1])

# 반환값 출력
print(in_stock(n))
