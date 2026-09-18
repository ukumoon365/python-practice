# 최고, 최저 점수
# 1. 시나리오 번호 입력
# 2. 해당 리스트의 최고 점수와 최저 점수 출력

# 3차원 리스트
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 40],
    [42],
]
# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# max, min 시퀀스 사용으로 최댓값,최솟값 출력
print(f"최고: {max(scores)}")
print(f"최저: {min(scores)}")
