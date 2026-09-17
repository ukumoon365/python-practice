# 비밀번호 확인

"""
1. 비밀번호를 입력받는다
2. 설정된 비밀번호와 맞는 지 비교한다
   맞으면 -> 로그인 성공! / 프로그램 종료
   틀리면 -> 틀렸습니다. 남은 기회 n번(3번) / 기회 1번 차감
             모든 기회 차감시 -> 계정이 잠겼습니다
"""
password = "python" # 비밀번호 설정

chance = 3  # 기회 3번 설정

while True:
    chance -= 1 # 기회 1회 차감
    input_password = input()
    if input_password == password:
        print("로그인 성공!")
        break   # 반복 종료
    else:   # 비밀번호가 틀렸을 경우
        if chance > 0:  # 기회가 남았을 경우
            print(f"틀렸습니다. 남은 기회: {chance}번")
        else:   # 남은 기회가 없을 경우
            print("계정이 잠겼습니다")
            break   # 반복 종료