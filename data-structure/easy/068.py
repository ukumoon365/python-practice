# 학생 점수 수정
# 1. 이름, 점수 입력
# 2. 딕셔너리의 해당 학생 점수 수정
# 3. 결과 출력

# 학생 점수 정보 딕셔너리
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}

# 이름, 점수 입력
name = input()
new_score = int(input())

# 입력된 이름의 점수 수정
scores[name] = new_score

# 결과 출력
print(f"{name}: {scores[name]}")