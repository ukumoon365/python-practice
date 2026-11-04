# 점수 통계
# 1. 시나리오 번호 입력
# 2. 합계, 평균, 최고, 최저 값 계산
# 3. 결과 출력

# 3개의 시나리오
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 합계, 평균, 최고, 최저 값 각각 변수로 저장
total = sum(scores.values())
average = total / len(scores)
max_score = max(scores.values())
min_score = min(scores.values())

# 결과 출력
print(f"합계: {total}")
print(f"평균: {average:.1f}")
print(f"최고: {max_score}")
print(f"최저: {min_score}")