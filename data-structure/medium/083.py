# 두 학기 학생 명단 비교
# 1. 시나리오 번호 입력
# 2. 두 학기 학생 명단 비교 
#   1) 각 비교 결과에 맞는 리스트 생성 및 명단 추가
# 3. 결과 출력

# 두 학기 학생 명단 딕셔너리
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95, "예준": 60},
    {"A": 85, "B": 95, "C": 75},
    {"Y": 60},
]
# 시나리오 번호 입력
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 컴프리헨션으로 순회하며 해당 학생 리스트에 추가
only_s1 = [name for name in s1 if name not in s2]
only_s2 = [name for name in s2 if name not in s1]
both = [name for name in s1 if name in s2]

# 결과 출력
print(f"1학기만: {' '.join(only_s1)}")
print(f"2학기만: {' '.join(only_s2)}")
print(f"양학기: {' '.join(both)}")