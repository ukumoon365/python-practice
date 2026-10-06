# zip + 컴프리헨션 
# 1. 시나리오 번호 입력
# 2. names와 scores를 순회 / zip으로 같은 인덱스 끼리 묶음 / f-string로 문자열 변환 / 공백 구분으로 결과 출력 

# 이름, 점수 3차원 리스트
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78, 95, 88],
    [100, 200],
    [42],
]

# 시나리오 번호 입력
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 두개의 리스트 순회 컴프리헨션 및 결과 출력
print(" ".join([f"{name}={score}" for name, score in zip(names, scores)]))