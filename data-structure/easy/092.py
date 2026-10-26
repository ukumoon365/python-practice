# 두 set의 교집합
# 1. 시나리오 번호 입력
# 2. 교집합 정렬
# 3. 결과 출력

# 2개의 set
a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"a", "b", "c", "d"},
    {"x", "y", "z"},
]
b_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"c", "d", "e", "f"},
    {"1", "2", "3"},
]

# 시나리오 번호 입력
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 두 교집합의 정렬
sorted_intersection = sorted(a&b)

# 결과 출력
print(' '.join(sorted_intersection))