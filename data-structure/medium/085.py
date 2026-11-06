# 등급별 학생 그룹회
# 1. 시나리오 번호 입력
# 2. 해당 딕셔너리 순회
#   1) 성적 비교 및 등급 측정
# 3. 등급 딕셔너리 순회
#   1) 결과 출력

# 3개의 시나리오
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95, "예준": 50},
    {"A": 78, "B": 95, "C": 55},
    {"윤서": 100, "지우": 95, "민준": 90},
]

# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 등급 딕셔너리
grades = {"A": [], "B": [], "C": [], "F": []}

# 딕셔너리 순회 for문
for name, score in scores.items():
    # 성적 비교 if문 / 등급 측정
    if score >= 90:
        grades["A"].append(name)
    elif score >= 80:
        grades["B"].append(name)
    elif score >= 70:
        grades["C"].append(name)
    else:   # 70 미만 점수
        grades["F"].append(name)

# 등급 딕셔너리 순회
for grade, names in grades.items():
    # 결과 출력
    if names:
        print(f"{grade}: {' '.join(names)}")
    else:
        print(f"{grade}:")