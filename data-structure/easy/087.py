# 회원 명단 확인
# 1. 이름 입력
# 2. 이름 유무 판별
# 3. 결과 출력

# 명단 리스트
members = {"윤서", "지우", "민준", "서윤", "도윤"}

# 이름 입력
name = input()

# 해당 명단 유무 확인 if문
if name in members:
    print("있음")
else:
    print("없음")