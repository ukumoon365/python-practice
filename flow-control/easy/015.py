# 성적 등급
# 1. 성적 입력
# 2. 성적에 따른 등급 분별
# 3. 결과 출력

score = int(input())

# 입력 받은 점수(score)에 따라 등급 분별 if문
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else: # 60미만일 경우
    grade = "F"

#결과 출력
print("점수:",score)
print("등급:",grade)