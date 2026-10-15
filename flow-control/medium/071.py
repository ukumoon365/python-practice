# 택시비 계산
# 1. 거리 및 시간을 입력
# 2. 2km 초과 판별
#   1) 초과 거리 당 1000원 추가
# 3. 시간이 22시 이상 6시 미만일 경우 판별
#   1) 총 요금에 야간 할증 20% 추가 
# 4. 결과 출력

# 거리 및 시간 입력
distance = float(input())
hour = int(input())

basic_charge = 4800      # 기본 요금 (2km까지 포함)
extra_charge = 0         # 추가 요금 0 초기 설정

# 주행거리 2km 초과 판별 if문
if distance > 2:                    # 주행 거리 2km 초과
    extra_charge = int((distance - 2) * 1000)      # 초과 거리 당 1000원 추가

# 총합 금액 계산
total_charge = basic_charge + extra_charge

# 결과 출력
print(f"기본요금: {basic_charge}원")
print(f"추가요금: {extra_charge}원")
if hour < 6 or hour >= 22:             # 시간이 22시 이상 6시 미만 야간일 때만
    night_charge = int(total_charge * 0.2)
    print(f"야간 할증 (20%): {night_charge}원")
    total_charge = night_charge + total_charge
print(f"총 택시비: {total_charge}원")