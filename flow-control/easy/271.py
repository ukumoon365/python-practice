# K 초과 원소만 합산
# 1. 정수 입력
# 2. 리스트 순회
#   1) k 초과값 누적합
# 3. 결과 출력

# 숫자 리스트
nums = [3, -2, 5, 0, -7, 4, -1, 6]

# 정수 입력
k = int(input())

# 누적합 변수 초기화
total_sum = 0

# 리스트 순회 for문
for nums_element in nums:
    # k 이하 판별 if문
    if nums_element <= k:   # k값 이하
        continue
    else:   # k값 초과
        total_sum += nums_element

# 결과 출력
print("합계:", total_sum)