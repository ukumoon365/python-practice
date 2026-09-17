# 배터리 잔량 확인
# 1. 배터리 잔량 입력
# 2. 배터리 잔량에 따른 충전 상태 판단 및 결과 출력

# 배터리 잔량 입력
battery = int(input())

# 배터리 잔량(battery)에 따라 충전 상태 판단
if battery <= 20:
    print("충전 필요")
else:
    print("배터리 충분")
