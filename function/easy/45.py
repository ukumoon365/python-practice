# global 키워드로 카운터 증가
# 1. 카운트 함수 정의
# 2. 정수 입력
# 3. n번 반복하며 함수 호출
# 4. 카운트 변수 출력

# 카운트 함수 정의
def increase():
    """
    전역 변수 count 호출 횟수 카운트 함수
    
    Global:
        count (int): 카운트 횟수
    
    Returns:
        None
    """ 
    global count

    count += 1

# 카운트 변수
count = 0

# 정수 입력
n = int(input())

# n번 함수 호출
for _ in range(n):
    increase()

# 결과 출력
print(count)