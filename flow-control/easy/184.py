# 숫자 합 게임
# 1. 숫자 개수 n 입력
# 2. n 만큼 반복
#    1) 정수를 입력 
#    2) 양수끼리 ,음수끼리 합 / 전체 합
# 3. 결과 값 출력

# 정수 입력
n = int(input())

# 양수, 음수, 누적합 변수 초기화
positive_sum_num = 0
negative_sum_num = 0
total_sum_num = 0

# n번 반복 for문
for i in range(n):
    # 정수 입력
    num = int(input())

    # 양수, 음수 판별 if문
    if num >= 0:
        positive_sum_num += num
    elif num < 0: 
        negative_sum_num += num

    # 누적합 계산
    total_sum_num += num

# 결과 출력
print(f"양수 합: {positive_sum_num}")
print(f"음수 합: {negative_sum_num}")
print(f"전체 합: {total_sum_num}")  