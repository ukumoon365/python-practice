# 최고점 학생 찾기
# 1. 시나리오 번호 입력
# 2. 딕셔너리 순회
#   1) 최고점 비교
# 3. 결과 출력

# 3개의 학생 이름, 점수 딕셔너리
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]

# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 최고점, 최고점 학생 변수 초기값 설정
top_name = ""
top_score = 0

# 딕셔너리 순회 / 최고점 비교
for name, score in scores.items():
    if top_score < score:
        top_score = score
        top_name = name

# 결과 출력
print(f"{top_name}: {top_score}")
    