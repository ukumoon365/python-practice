# 음수 입력시 종료
"""
# 1. 숫자를 입력받는다
# 2. 양수가 입력 되면 -> 누적 합산 -> 1번 반복
# 3. 음수가 입력되면 -> 반복 종료/ 합계 출력/ 프로그램 종료
"""

total = 0 # 종합 누적 변수 초기화

# 무한 루프로 음수를 입력 받을 때 까지 반복
while True:
    number = int(input())
    if number >= 0:         # 양수
        total += number     # 누적 합산
    else:                   # 음수
        print(f"합계: {total}")     # 합계 값 출력
        break                       # 프로그램 종료