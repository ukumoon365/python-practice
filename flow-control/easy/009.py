# 가위바위보 (컴퓨터는 바위 고정)
"""
1. 컴퓨터 바위 고정 / 유저 값 입력
2. 입력값에 따라 승리 판단
3. 결과 출력
"""
# 컴퓨터 값 초기화
computer = "바위"

# 유저 값 입력
user = input()

# 입력값(user)에 따라 승리 판단
if user == "바위":
    result = "비겼습니다"
elif user == "가위":
    result = "졌습니다"
elif user == "보":
    result = "이겼습니다"
else: # 그 외 입력은 잘못된 입력입니다
    result = "잘못된 입력입니다"

# 결과 출력
print ("컴퓨터: 바위")
print ("나:",user)
print ("결과:",result)