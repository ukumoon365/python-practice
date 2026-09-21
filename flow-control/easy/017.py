# 교통수단 추천
# 1. 거리를 입력
# 2. 거리에 따른 교통수단 구분
# 3. 결과 출력

# 거리 입력
distance = float(input())

# 거리에 따른 교통수단 구분 if문
if distance >= 20:
    transportation = "지하철"
elif distance >= 5:
    transportation = "버스"
elif distance >= 2:
    transportation = "자전거"
else: # 그 외 2km 미만
    transportation = "도보"

# 결과 출력
print(f"거리: {distance}km")
print(f"추천 교통수단: {transportation}")