# 평균 구하기
# 1. 정수 입력
# 2. 입력 값이 0이 될 때 까지 반복
#   1) 누적합
#   2) 횟수 카운트
#   3) 정수 입력
# 3. 결과 출력

# 정수 입력
num = int(input())

# 누적합 변수 초기화
total = 0
# 카운트 변수 초기화
count = 0

# 입력 값이 0이 될 때까지 반복 while문
while num != 0:
    total += num    # 누적합
    count += 1  # 횟수 카운트
    num = int(input())  # 정수 입력

# 결과 출력 / 횟수 0일 경우 판별 if문
if count == 0:
    print("입력한 숫자가 없습니다.") 
else:
    print(f"평균: {total / count}") 