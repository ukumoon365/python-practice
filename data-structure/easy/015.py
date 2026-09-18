# 점수 총합과 평균
# 1. 시나리오 번호를 입력
# 2. 선택된 시나리오의 총합, 평균계산
# 3. 결과 출력

# 3차원 데이터 리스트
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 총합, 평균 계산
total_sum = sum(scores)
averge = total_sum / len(scores)

# 결과 출력
print(f"총합: {total_sum}")
print(f"평균: {averge:.1f}")