# 놀이공원 입장료
# 1. 나이와 인원 수 입력
# 2. 나이에 따라 입장료 계산
# 3. 기본 입장료 입력
# 4. 인원 수가 10명 이상일 경우 20% 할인
# 5. 최종 입장료 입력

# 나이, 인원수 입력
age = int(input())
group_count = int(input())

# 나이 구분 if문
if age <= 3:
    price = 0
elif age <= 12:
    price = 15000
elif age <= 18:
    price = 20000
elif age <= 64:
    price = 30000
else:   # 65세 이상
    price = 10000

# 기본 입장료 출력
print(f"기본 입장료: {price}원")

# 인원 수 10명 이상 판별 if문
if group_count >= 10:
    # 20% 할인 
    price = int(price * 0.8)
    print("단체 할인 적용 (20%)!")
    print(f"1인 할인가: {price}원")

# 최종 금액 출력
print(f"총 입장료: {price * group_count}원")