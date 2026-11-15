# 두 학기 명단 분류
# 1. 시나리오 번호 입력
# 2. 조건에 맞는 값 출력

# 3개의 시나리오 set
s1_sets = [
    {"윤서", "지우", "민준"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "민준", "도윤", "예준"},
    {"A", "B", "C"},
    {"P", "Q"},
]

# 시나리오 번호 입력
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 결과 출력
print(f"1학기만: {' '.join(sorted(s1 - s2))}")
print(f"2학기만: {' '.join(sorted(s2 - s1))}")
print(f"양학기: {' '.join(sorted(s1 & s2))}")