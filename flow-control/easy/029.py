# 놀이기구 탑승
# 1. 키 입력
# 2. 키 130 이상, 이하 판별
# 3. 부모 동반 여부 입력
# 4. 부모 동반 여부 및 키 150 이상, 이하 판별
# 5. 결과 출력

# 키 입력
height = int(input())

# 키가 130cm 이상인지 확인
if height >= 130:
    guardian = input()  # 보호자 동반 여부 확인
    if guardian.upper() == "Y":
        result = "보호자와 함께 탑승 가능합니다."
    elif height >= 150:  # 키가 150cm 이상 여부인지 확인 
        result = "혼자 탑승 가능합니다."
    else:
        result = "보호자가 필요합니다."
else:
    result = "탑승할 수 없습니다."

# 결과 출력
print(result)