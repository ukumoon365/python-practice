# 두 set의 합집합
# 1. 시나리오 번호 입력
# 2. 합집합 정렬
# 3. 결과 출력

# 2개의 set
a_sets = [
    {"윤서", "지우", "민준"},
    {"a", "b", "c"},
    {"1", "2", "3"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"x", "y", "z"},
    set(),
]

# 시나리오 번호 입력
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 합집합의 정렬
union = sorted(a|b)

# 결과 출력
print(" ".join(union))