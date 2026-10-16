# 성적 평가 및 수료 판정
# 1. 점수와 출석률을 입력
# 2. 점수에 따라 등급을 판별
# 3. 등급과 출석률에 따라 수료 결과 판별
# 4. 결과 출력

# 점수 및 출석률 입력
score = int(input())
attendance = int(input())

# 등급 판별 if문
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# 출석률 판별 if문
if attendance < 80:
    completion = "미수료 - 출석률 부족 (80% 이상 필요)"
elif grade == "F":
    completion = "미수료 - 성적 미달 (60점 이상 필요)"
else:
    completion = "수료를 축하합니다!"

# 결과 출력
print(f"등급: {grade}")
print(completion)