# 중고차 가격 산정
# 1. 신차 가격,연식,주행거리,사고유무를 입력
# 2. 감가율(연식,주행거리,사고유무) 계산
# 3. 총 감가율 계산
# 4. 예상 중고차 가격 계산
# 5. 결과 출력

# 신차 가격, 연식, 주행거리, 사고유무 입력
new_price = int(input())
year = int(input())
km = float(input())
accident = input()

# 연식 판별 if문
if year <= 3:
    year_depreciation = year * 10
elif year <= 7:
    year_depreciation = 3 * 10 + (year - 3) * 7
else:       # year > 7
    year_depreciation = 3 * 10 + 4 * 7 + (year - 7) * 5

# 주행거리 판별 if문
if km <= 5:
    km_depreciation = 0
elif km <= 10:
    km_depreciation = 5
else:       # km > 10
    km_depreciation = 10

# 사고 유무 판별 if문
if accident.upper() == "Y":
    accident_depreciation = 15
else:       # accident == "N"
    accident_depreciation = 0

# 총 감가 계산
total_discount = year_depreciation + km_depreciation + accident_depreciation
# 총 가격 계산
total_price = int(new_price * (1 - total_discount / 100))
# 예상 가격 계산
minimum_price = int(new_price * 0.1)

# 결과 출력
print("--- 감가 내역 ---")
print(f"연식 감가 ({year}년): {year_depreciation}%")
print(f"주행거리 감가: {km_depreciation}%")
print(f"사고 감가: {accident_depreciation}%")
print(f"총 감가율: {total_discount}%")
if total_price < minimum_price:
    print(f"예상 중고차 가격: {minimum_price}만원")
else:
    print(f"예상 중고차 가격: {total_price}만원")

    