# BMI 판정
# 1. 키, 몸무게 입력
# 2. BMI 계산
# 3. BMI값에 따라 판정
# 4. 결과 출력

# 키, 몸무게 입력
height = float(input())
weight = float(input())

# 입력 받은 키, 몸무게로 BMI 계산
height_m = height / 100 # cm에서 m으로 단위 변경 후 계산
BMI = weight / (height_m ** 2) 
BMI = round(BMI, 2) 

# bmi에 따라 판정 (bmi 수치가 큰 순서부터)
if BMI >= 25:
    result = "비만"
elif BMI >= 23:
    result = "과체중"
elif BMI >= 18.5:
    result = "정상"
elif BMI < 18.5:
    result = "저체중"

# 결과 출력
print(f"키: {height}cm, 몸무게: {weight}kg")
print(f"BMI: {BMI}")
print(f"판정: {result}")