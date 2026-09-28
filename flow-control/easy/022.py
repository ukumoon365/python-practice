# 온도별 옷차림 추천
# 1. 온도 입력
# 2. 온도별 옷차림 추천
# 3. 결과 출력

# 온도 입력
temp = float(input())

# 별로 옷차림 추천 (온도가 높은 순으로)
if temp >= 28:
    clothes = "민소매, 반바지"
elif temp >= 20:
    clothes = "반팔, 얇은 셔츠"
elif temp >= 10:
    clothes = "자켓, 가디건"
elif temp >= 5:
    clothes = "코트, 니트"
else:  # 5도 미만 -> 패딩,두꺼운 목도리
    clothes = "패딩, 두꺼운 목도리"

# 결과 출력
print(f"현재 기온: {temp}°C")
print(f"추천 옷차림: {clothes}")