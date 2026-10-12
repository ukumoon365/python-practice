# 점수 보너스
# 1. 시나리오 번호 입력
# 2. 해당 리스트의 각 점수에 10을 더해 값을 출력 
#    100을 넘기면 100으로 짜른 후 출력

# 3차원 리스트
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 최대 100 클리핑
score_clip = [min(score + 10, 100) for score in scores]

# 결과 출력
print(" ".join(map(str,score_clip)))