# 결석생 판별
"""
1. 이름을 입력
2. 해당 학생이 명단에 없으면 -> 결석
   있으면 -> 출석
"""
# 학생 명단
attendance = ["윤서", "민준", "도윤", "예준"]

# 이름 입력
name = input()

if name not in attendance:  # not in으로 명단에 없는 경우 먼저 탐색
    print("결석")
else:
    print("출석")