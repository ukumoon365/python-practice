# 점수 오름차순 정렬
# 1. 시나리오 번호 입력
# 2. 딕셔너리 순회 / 듀플로 정렬 / 리스트
# 3. 리스트 순회
#       1) 결과 출력

# 3개의 딕셔너리
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"A": 50, "B": 50, "C": 50},
]

# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 딕셔너리 순회 / 튜플로 오름차순으로 정렬 / 리스트화 컴프리헨션
pairs = sorted([(score, name) for name, score in scores.items()])

# 리스트 순회 for문
for score, name in pairs:
    # 결과 출력
    print(f"{name}: {score}")
