# 점수 내림차순 정렬
# 1. 시나리오 입력
# 2. 해당 시나리오의 점수를 내림차순으로 정렬
# 3. 결과 출력

# 3개의 점수 시나리오
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]

# 시나리오 번호 입력
t = int(input())
scores = data_sets[t]

# 내림차순으로 정렬
result = " ".join(map (str, sorted(scores, reverse=True)))

# 결과 출력
print(result)