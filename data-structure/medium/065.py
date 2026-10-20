# 최고점 학생 찾기
# 1. 시나리오 번호 입력
# 2. 딕셔너리 순회
#   # 1) 최고점 비교
#       1. 최고점 갱싱
# 3. 결과 출력

# 3개의 시나리오
data_sets = [
    [("윤서", 85), ("지우", 92), ("민준", 65), ("서윤", 78), ("도윤", 95)],
    [("A", 70), ("B", 90), ("C", 80)],
    [("solo", 70)],
]
# 시나리오 번호 입력
t = int(input())
students = data_sets[t]

# 최고점 변수 초기화
top_score = 0

# 딕셔너리 순회
for name, score in students:
    # 최고점 비교
    if top_score < score:
        # 최고점 갱신
        top_score = score
        top_name = name    

# 결과 출력
print(f"{top_name}: {top_score}")