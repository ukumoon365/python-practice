# global 키워드로 누적 합
# 1. 전역 변수 누적 합 함수 정의
# 2. 정수 입력 및 리스트화
# 3. 리스트 순회 및 함수 호출
# 4. 결과 출력

def add(n: int) -> None:
    """
    전역 변수 total에 누적 합 계산 함수

    Args:
        n (int): 입력 받은 정수

    Global:
        int: n값을 누적하여 합산하는 변수

    Returns:
        None
    """
    global total # 전역변수 사용 선언

    total += n


# 누적합 변수 초기화
total = 0

# 정수 입력 및 리스트화
nums = [int(x) for x in input().split()]

# 리스트 순회로 누적 합 계산
for n in nums:
    add(n)

# 결과 출력
print(total)