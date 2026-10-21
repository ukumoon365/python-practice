# set의 고유 원소 개수
# 1. 시나리오 번호 입력
# 2. 해당 set의 길이 출력

# 3개의 시나리오
data_sets = [
    {"apple", "banana", "cherry", "date"},
    {"single"},
    set(),
]
# 시나리오 번호 입력
t = int(input())
fruits = data_sets[t]

# 해당 set의 길이 출력
print(len(fruits))