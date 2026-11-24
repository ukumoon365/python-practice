# 명단표 출력
# 1. 시나리오 번호 입력
# 2. 두 시퀀스 set 변환 후 언패킹 / 순회
# 3. 결과 출력

# 3개의 시나리오
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
# 시나리오 번호 입력
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 튜플 순회 및 언패킹
for name, score in zip(names, scores):
    # 이름 , 점수 매칭 및 출력
    print(f"{name}: {score}")

