# 배송 방식
# 1. 무게, 옵션 입력
# 2. 무게에 따른 배송 방식 판별 
# 3. 옵션에 따른 배송 방식 판별 
# 4. 결과 출력

# 무게, 옵션 입력
weight = float(input())
option = input()

# 무게에 따른 배송 방식 if문 
if weight >= 2:
    # 옵션에 따른 배송 방식 if문
    if option.upper() == "Y": 
        print("택배(빠른 배송) - 5000원")
    else:
        print("택배(일반 배송) - 3000원")
else: #무게 2kg 미만
    # 옵션에 따른 배송 방식 if문
    if option.upper() == "Y":
        print("우편(등기) - 2000원")
    else:
        print("우편(일반) - 1000원")