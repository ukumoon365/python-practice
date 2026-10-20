# 학생 명단표
# 1. 시나리오 번호 입력
# 2. 딕셔너리 순회
#   1) 이름과 점수 출력

# 3개의 시나리오
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 해당 딕셔너리를 순회 for문
for name, score in scores.items():
    print(f"{name}: {score}") # 결과 출력

