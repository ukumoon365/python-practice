# 숫자 맞추기 게임

# 정답 변수 
answer = 42

# 무한 루프 / 입력값과 정답이 같을 경우 반복 종료
while True:
    num = int(input())  # 숫자를 입력 받는다

    # 정답과 입력 받은 수를 비교한다       
    if num < answer:    # 입력값이 정답보다 작은 경우
        print("더 큰 수를 입력하세요")
    elif num > answer:  # 입력값이 정답보다 큰 경우
        print("더 작은 수를 입력하세요")
    else:   # 정답 
        print("정답입니다!")
        break