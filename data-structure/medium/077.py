# 특정 점수를 받은 학생들
# 1. 점수 입력
# 2. 해당 점수를 가진 학생 리스트 컴프리헨션
# 3. 결과 출력

# 학생 이름, 성적 딕셔너리
scores = {"윤서": 85, "지우": 92, "민준": 85, "서윤": 78, "도윤": 92, "예준": 65}

# 점수 입력
taget_score = int(input())

# 특정 점수의 학생 리스트
students = [name for name, score in scores.items() if score == taget_score]

# 학생 유무 판별 if문
if students:
    print(" ".join(students))
else:
    print("없음")