# 디지털 시계
# 1. 초 입력
# 2. 입력 받은 초를 시, 분, 초로 변환
# 3. 결과 출력

# 초 입력
total_seconds = int(input())

# 시, 분, 초로 변환
hour = total_seconds // 3600
total_seconds %= 3600
minute = total_seconds // 60
seconds = total_seconds % 60

# 결과 출력
print(f"{hour:02d}:{minute:02d}:{seconds:02d}")