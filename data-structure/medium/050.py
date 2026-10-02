# enumerate + 컴프리헨션
# 1. 시나리오 번호 입력
# 2. 해당 리스트를 순회 하며 인덱스와 값을 추출
# 3. 값을 문자열로 변환하여 공백 구분으로 출력

# 3차원 리스트
data_sets = [
    ["red", "green", "blue", "yellow", "purple"],
    ["apple", "banana", "cherry"],
    ["single"],
]

# 시나리오 번호 입력
t = int(input())
items = data_sets[t]

# 리스트 순회 인덱스와 값을 추출 컴프리헨션 및 문자열 변환 출력
print(" ".join([f"{i}:{value}" for i,value in enumerate(items)]))