# 명단 역순 출력
# 1. 시나리오 번호 입력 
# 2. 선택된 시나리오의 명단을 역순으로 변환 / names.reverse()
# 3. 결과 출력 

# 명단 시나리오
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤", "예준"],
    ["red", "green", "blue"],
    ["혼자"],
]

# 시나리오 번호 입력
t = int(input())
names = data_sets[t]

# 역순 정렬
names.reverse()

# 결과 출력
print(" ".join(names))