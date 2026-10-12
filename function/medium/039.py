# 전역변수만으로 계산
# 1. 세금 계산 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def tax_of() -> int:
    """ 
    세금 계산 함수 
    
    Globals:
        amount (int): 금액
        rate (int): 세율 %

    Return
        int: 계산 결과값
    """
    return amount * rate // 100

# 정보 입력
parts = input().split()
amount = int(parts[0])
rate = int(parts[1])

# 결과 출력
print(tax_of())
