# 가위바위보
# 1. 유저 선택 입력
# 2. 승패 판정 
# 3. 결과 출력

# 유저 선택 입력
user = int(input())

# 컴퓨터 바위 고정
computer = 2

choices = {1: "가위", 2: "바위", 3: "보"}       # 가위바위보 리스트

# 입력값 리스트 in 유무 판별 if문
if user in choices:
    print(f"당신: {choices[user]} / 컴퓨터: {choices[computer]}")
    if user == 1:
        print("아쉽게도 졌습니다. 😢")
    elif user == 2:
        print("무승부입니다! 😐")
    else:       # user == 3 
        print("축하합니다! 당신이 이겼습니다! 🎉")
else:   # 잘못된 입력
    print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")