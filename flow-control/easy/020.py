# 요일 판정
# 1. 요일 번호 입력
# 2. 해당 요일 번호에 따라 요일 구분
# 3. 결과 출력

# 요일 번호 입력 
day = int(input())

# 요일 번호에 따라 요일 구분
if day == 1:
    result = "월요일"
elif day == 2:
    result = "화요일"
elif day == 3:
    result = "수요일"
elif day == 4:
    result = "목요일"
elif day == 5:
    result = "금요일"
elif day == 6:
    result = "토요일"
elif day == 7:
    result = "일요일"
else:  # 1~7이 아닌 모든 입력 값은 거짓
    result = ""

# 결과 출력
if result: 
    print(f"{day} → {result}")
else: # 1~7이 아닌 모든 입력 값 예외 처리
    print("잘못된 입력입니다.")