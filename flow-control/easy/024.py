# 입장 판정
# 1. 나이, 티켓값 입력
# 2. 나이와 티켓 유무에 따라 입장 판정
# 3. 결과 출력

# 나이, 티켓 유무 입력
age = int(input())
ticket = input()

# 18세 이상인지 확인 if문
if age >= 18:
    # 티켓 유무 확인 이중 if문
    if ticket == "Y":
        print("입장 가능합니다.")
    else:
        print("티켓을 구매해주세요.")
else:  #18세 미만
    print("18세 미만은 입장할 수 없습니다.")