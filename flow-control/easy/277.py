# 택시 배차 시스템
# 1. 배차 가능 여부, 목적지 입력
# 2. 목적지 입력 여부 판별
#   1) 배차 가능 여부 판별
# 결과 출력

# 배차 가능 여부 입력
available = input() == "True"
# 목적지 입력
destination = input()

# 목적지 입력 여부 판별 if문
if available:
    # 배차 가능 여부 판별 if문
    if destination:
        print("운행 시작")
    else:
        print("목적지를 입력하세요")
else:
    print("차량 대기 중")

