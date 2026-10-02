# 영화 추천
# 1. 장르 및 나이 입력
# 2. 장르, 나이에 따른 영화 추천
# 3. 결과 출력

# 장르 및 나이 입력
genre = input()
age = int(input())

# 19세 이상을 변수로 지정 -> 연산 반복 방지
age_adult = age >= 19

# 장르(액션,로맨스)와 나이에 따라 영화 추천 if문
if genre == "액션":  # 액션 선택 
    if age_adult:  # 19세 이상
        movie = "추천: 존 윅"
    else:
        movie = "추천: 스파이더맨"
elif genre == "로맨스":  # 로맨스 선택
    if age_adult:  # 19세 이상
        movie = "추천: 노트북"
    else:
        movie = "추천: 너의 이름은"
else:  # 그 외 장르
    movie = "해당 장르의 추천 영화가 없습니다."
    
# 결과 출력
print(movie)