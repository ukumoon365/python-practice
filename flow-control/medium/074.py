# bmi 판정
# 1. 키, 몸무게, 나이를 입력
# 2. bmi 계산
# 3. 나이와 bmi 계산 결과에 따라 저체중, 정상, 과체중, 비만을 판단
# 4. 결과 출력

# 키, 몸무게, 나이 입력
height = float(input())
weight = float(input())
age = int(input())

# bmi 계산
bmi = weight / ((height/100) ** 2)

# 나이와 bmi 계산 결과에 따라 판단
if age >= 20:     # 성인 
    if bmi < 18.5:
        result = "저체중"
    elif bmi < 23:
        result = "정상"
    elif bmi < 25:
        result = "과체중"
    else:        # bmi 25 이상
        result = "비만"
else:           # age 20 미만
    if bmi < 17:
        result = "저체중 (청소년 기준)"
    elif bmi < 23:
        result = "정상 (청소년 기준)"
    else:       # bmi 23 이상
        result = "과체중 주의 (청소년 기준)"

# 결과 출력
print(f"BMI: {round(bmi, 2)}")
print(f"판정: {result}")
