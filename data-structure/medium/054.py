# 학생별 등급 매핑
# 1. 시나리오 번호 입력
# 2. 두 리스트를 하나의 딕셔너리 정리
# 3. 딕셔너리 순회 및 출력

# 이름 3차원 리스트
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
# 점수 3차원 리스트
scores_sets = [
    [85, 92, 65, 78, 95],
    [100, 55, 72],
    [85],
]

# 시나리오 번호 입력
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 이름과 성적을 등급별로 딕셔너리로 정리 컴프리헨션
students = {
    name: ("A" if score >= 90 else 
           "B" if score >= 80 else
           "C" if score >= 70 else "F") 
for name, score in zip(names, scores)}

# 딕녀서리 순회 / 결과 출력
for name, grade in students.items():
    print(f"{name}: {grade}")