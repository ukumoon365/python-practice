# 할인 적용
# 1. 회원 여부 입력
# 2. 회원 여부 판별
#   회원 일 시 vip 값 입력
# 3. vip 판별
# 4. 결과 출력

# 회원 여부 입력
is_member = input()

# 회원 판별 if문
if is_member.upper() == "Y":
    # vip 판별 if문
    is_vip = input()  # vip 여부 
    if is_vip.upper() == "Y":
        print("20% 할인 적용")
    else:  # vip가 아닐 경우
        print("10% 할인 적용")
else:  # 회원이 아닐 경우
    print("할인 없음")