# 동전 모으기
# 1. 목표 금액 입력
# 2. 입력 금액이 목표 금액을 초과할 때까지 반복
#   1) 금액 입력
#   2) 금액 누적합
# 3. 결과 출력

# 목표 금액 입력
goal = int(input())

# 현재 금액 변수 초기화
saved = 0

# 입력 금액이 목표 금액을 초과할 때까지 반복 while문
while saved < goal:
    print(f"현재: {saved}원 / 목표: {goal}원")  #  현재 상황 출력
    
    # 금액 입력
    deposit = int(input())
    # 누적합 계산
    saved += deposit

# 결과 출력
print(f"현재: {saved}원 / 목표: {goal}원")  
print(f"목표 달성! 총 {saved}원을 모았습니다.")