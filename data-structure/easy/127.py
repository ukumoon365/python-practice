# 평균 점수
# 1. 시나리오 번호 입력
# 2. 평균 계산
# 3. 결과 출력

# 3개의 시나리오
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 평균 계산
average = sum(scores) / len(scores)
# 결과 출력
print(f"평균: {average:.1f}")
