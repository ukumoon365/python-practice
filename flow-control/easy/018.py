# 영화 요금 계산
# 1. 나이 입력
# 2. 나이에 따른 요금 계산
# 3. 결과 출력

# 나이 입력
age = int(input())

# 나이에 따른 요금 계산 if문
if age >= 65:
    classification = "경로"
    price = 5000
elif age >= 20:
    classification = "성인"
    price = 12000
elif age >= 14:
    classification = "청소년"
    price = 8000
elif age >= 8:
    classification = "어린이"
    price = 5000
else:  # 7세 이하 -> 무료,0원
    classification = "무료"
    price = 0

# 결과 출력
print(f"나이: {age}세")
print(f"구분: {classification}")
print(f"요금: {price}원")