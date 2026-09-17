# 회원 명단 확인
"""
1. 이름을 입력
2. 해당 이름이 있으면 -> 있음
   없으면 -> 없음
"""
# 회원 명단
members = ["윤서", "지우", "민준", "서윤", "도윤"]

# 이름 입력
name = input()

# 명단 확인
if name in members:
    print("있음")
else:
    print("없음")