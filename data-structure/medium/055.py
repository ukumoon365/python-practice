# 합격자만 필터
# 1. cutoff 값 입력
# 2. cutoff 이상 점수의 학생 딕녀너리화 (컴프리헨션)
# 3. 딕셔너리 순회 및 결과 출력

# 학생 이름, 점수 딕셔너리
students = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}

# cutoff 값 입력
cutoff = int(input())

# 입력 받은 점수의 이상인 학생 딕셔너리
cutoff_students = {name: score 
                   for name, score in students.items() if score >= cutoff}

# 딕셔너리 순회 / 결과 출력
for name, score in cutoff_students.items():
    print(f"{name}: {score}")