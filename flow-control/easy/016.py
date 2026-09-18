# 계절 판별
# 1. 월 입력
# 2. 월에 따라 계절 판별
# 3. 결과 출력

# 월 입력
month = int(input())

# 월(month)에 따라 계절 판별 if문
if 3 <= month <= 5:
    season = "봄"
elif 6 <= month <= 8:
    season = "여름"
elif 9 <= month <= 11:
    season = "가을"
else: # 그 외 12,1,2월
    season = "겨울"

# 결과 출력
print (f"{month}월은 {season}입니다.")