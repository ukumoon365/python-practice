# list → set으로 중복 제거 후 개수
# 1. 정수 입력
# 2. 해당 인덱스 리스트 집합 변환
# 3. 결과 출력

# 데이터셋
datasets = [
    ["apple", "banana", "apple", "cherry"],
    [1, 2, 1, 2, 1, 2, 3],
    ["A", "B", "C", "D", "E"]
]

# 정수 입력
t = int(input())

# 지정된 리스트를 집합으로 변환
dataset_set = set(datasets[t])

# 결과 출력
print(len(dataset_set))