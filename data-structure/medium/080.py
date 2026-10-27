# 학생별 평균 점수
# 1. 학생 이름 입력
# 2. 학생 유무 확인
# 3. 평균 계산
# 4. 결과 출력

# 학생 이름, 점수 딕셔너리
students = {
    "윤서": [85, 90, 78],
    "지우": [92, 88, 95],
    "민준": [65, 70],
    "서윤": [80, 80, 80, 80],
}

# 이름 입력
name = input()

# 해당 학생 유무 확인 if문
if name in students:
    scores = students[name]
    # 학생 별 평균 점수 계산
    average = sum(scores) / len(scores)
# 결과 출력 (소수점 첫째자리까지)
    print(f"평균: {average:.1f}")
else:
    print("해당 학생 없음")