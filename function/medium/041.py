# 전역 리스트 읽어 합산
# 1. 전역변수 합산 함수 정의
# 2. 정수 입력
# 3. 함수 호출 및 출력 
def total() -> int:
    """
    전역 변수 합을 반환 함수  

    Globals:
        nums(int): 정수 리스트

    Return:
        int: 리스트의 총합
    """
    return sum(nums)

# 정수 입력 및 리스트화
nums = [int(x) for x in input().split()]

# 함수 호출 및 출력
print(total())