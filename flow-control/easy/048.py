# 최대값 찾기
# 1. 정수 입력
# 2. -1을 입력 받을 때까지 반복
#      1) 최대값과 비교
#           1. 최대값 갱신
#      2) 정수 입력
# 3. 결과 출력

# 최대값 변수 초기화
max_val = -1 

# 정수 입력
number = int(input())

# -1을 입력 받을 때까지 반복
while number != -1:
    # 최대값 비교 if문
    if max_val < number: 
        max_val = number    # 최대값 갱신
    # 정수 입력
    number = int(input())

# 결과 출력 / 입력값 없음 방지 if문
if max_val == -1:
    print("입력한 숫자가 없습니다.")
else:
    print(f"최대값: {max_val}")