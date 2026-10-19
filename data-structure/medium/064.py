# zip 결과는 tuple
# 1. 시나리오 번호 입력
# 2. 두개의 리스트 zip으로 패킹 및 순회
# 3. 결과 출력

# 두개의 시나리오 리스트
names_sets = [
    ["A", "B", "C", "D", "E"],
    ["윤서", "지우", "민준"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78],
    [85, 92, 65],
    [42],
]

# 시나리오 번호 입력
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# zip 시퀀스로 묶음 / 순회 for문
for name, score in zip(names, scores):
    # 출력
    print(f"{name}: {score}")
