# 계절별 인사
# 1. 월 입력 받기
# 2. 계절에 맞는 인사말 출력


# 월 입력
month = int(input())

# 계절과 인삿말 리스트 정리
season_list = ["봄입니다.", "여름입니다.", "가을입니다.", "겨울입니다."]
greeting_list = ["따뜻한 봄이에요! 꽃구경 가세요 🌸", "더운 여름이에요! 시원하게 보내세요 🌊", "선선한 가을이에요! 단풍 구경 가세요 🍂", "추운 겨울이에요! 따뜻하게 입으세요 ⛄"]

# 계절 판별 if문 / 계절에 맞는 인사말 출력
if month in (3, 4, 5):      # 3, 4, 5일 경우
    print(season_list[0])
    print(greeting_list[0])
elif month in (6, 7, 8):    # 6, 7, 8일 경우
    print(season_list[1])
    print(greeting_list[1])
elif month in (9, 10, 11):  # 9, 10, 11일 경우
    print(season_list[2])
    print(greeting_list[2])
elif month in (12, 1, 2):   # 12, 1, 2일 경우
    print(season_list[3])
    print(greeting_list[3])
else:                       # 그 외
    print("잘못된 입력입니다.")
