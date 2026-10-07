# global 키워드로 조건부 카운트
# 1. 전역 변수 positive_count를 n이 양수일 때만 1 늘리는 카운트 함수 정의
# 2. 정수 입력
# 3. 숫자 리스트 순회
# 4. 결과 출력

def check(n):
    """
    전역 변수 positive_count를 n이 양수일 때만 1 늘리는 카운트 함수

    Global:
    positive_count (int): n값이 양수일 때 +1 카운트 하는 전역 변수

    Args:
    n (int): 입력 받을 숫자

    """
    global positive_count

    if n > 0:   # 양수일 때만 카운트
        positive_count += 1

# 카운트 변수 초기화
positive_count = 0

# 정수 입력
nums = [int(x) for x in input().split()]

# 숫자 리스트 순회
for n in nums:
    check(n)

# 결과 출력
print(positive_count)