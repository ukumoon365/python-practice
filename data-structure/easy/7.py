# 특정 이름의 위치
"""
1. 이름을 입력 
2. 리스트에 명단이 있는지 확인
   있으면 -> n번대에 있습니다
   없으면 -> 명단에 없습니다
"""
# 명단
names = ["윤서", "지우", "민준", "서윤", "도윤", "예준"]

# 이름 입력
name = input()

# 명단 확인
if name in names :
    name_number = names.index(name) + 1     # 입력 받은 이름을 .index를 통해 추출, index는 0부터 시작하기에 + 1
    print(f"{name_number}번째에 있습니다")
else:
    print("명단에 없습니다")