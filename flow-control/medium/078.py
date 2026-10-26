# 환전 프로그램
# 1. 통화((1=달러, 2=엔, 3=유로, 그 외= 잘못된 입력) 입력
#    원화 금액을 입력
# 2. 선택된 통화에 따라 환전 금액 및 수수료 계산
# 3. 결과 출력 (환전 금액, 수수료, 실 지불 금액)

# 통화 입력
currency = int(input())
# 원화 입력
krw = int(input())

currency_map = {1: 1350, 2: 9, 3: 1450}     # 환율 딕셔너리화

# 통화 선택 판별 if문
if currency in currency_map:
    # 각 통화에 맞는 환율 적용
    if currency == 1:
        change_price = krw / currency_map[1] 
        change_price = round(change_price, 2)
        currency_unit = "달러"
    elif currency == 2:
        change_price = krw / currency_map[2]
        currency_unit = "엔"
    else:       # currency ==3:
        change_price = krw / currency_map[3]
        currency_unit = "유로"
    fee = int(krw * 0.015)      # 수수료 
    total_price = (krw + fee)   # 실 지불 금액

    # 결과 출력
    print(f"환전 금액: {change_price} {currency_unit}")
    print(f"수수료 (1.5%): {fee}원")
    print(f"실 지불 금액: {total_price}원")   
else:   # 그 외 입력
    print("잘못된 통화 선택입니다.")