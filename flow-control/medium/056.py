# 간단한 메뉴 시스템
# 1. 메뉴를 출력한다
# 2. 숫자를 입력 받는다
# 3. 선택 된 메뉴의 값을 출력한다
# 4. q가 입력 될 때 까지 1~3번을 반복한다

menu_list = {1: "안녕하세요!", 2: "오늘 날씨가 좋습니다!"}      # 메뉴 딕셔너리 정리

while True:
    print("===== 메뉴 =====")       # 메뉴 출력
    print("1. 인사")
    print("2. 날씨")
    print("q. 종료")
    print("================")

    select = input()               # 사용자 선택 입력
    
    if select == "1":
        print(menu_list[1])
    elif select == "2":
        print(menu_list[2])
    elif select == "q":
        print("프로그램을 종료합니다")
        break   # 반복 종료
    else:       # 그 외 입력
        print("잘못된 입력입니다")