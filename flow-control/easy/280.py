# 식물 물주기 도우미
# 1. 흙 상태, 햇빛 세기 입력
# 2. 물 정도 판별 
# 3. 결과 출력

# 상태 입력
soil_dry = input() == "True"
strong_sun = input() == "True"

# 물 정도 판별 if문 / 결과 출력
if soil_dry:
    if strong_sun:
        print("물 듬뿍")
    else:
        print("물 조금")
else:
    print("물 안 줘도 돼요")