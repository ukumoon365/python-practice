# tuple 사전식 정렬
# 1. 시나리오 번호 입력
# 2. 리스트 오름차순 정렬
# 3. 리스트 순회 및 출력

# 3차원 리스트
data_sets = [
    [(85, "윤서"), (92, "지우"), (65, "민준"), (78, "서윤"), (95, "도윤")],
    [(80, "A"), (70, "B"), (90, "C")],
    [(50, "혼자")],
]

# 시나리오 번호 입력
t = int(input())
students = data_sets[t]

# 오름차순 정렬
sorted_students = sorted(students)

# 리스트 순회 및 출력
for score, name in sorted_students:
    print(f"{name}: {score}")