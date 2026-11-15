# 헬스장 출석률 계산
# 1. 출석 기록 입력
# 2. 출석률의 문자열 순회
#    총 출석한 날 / 100 -> 출석률
# 3. 결과 출력

# 출석 기록 입력
record = input()

# 카운트 변수 초기화
attendance_count = 0

# 문자열 순회
for attendance in record:
    if attendance == "O":   # 출석한 날만 카운트
        attendance_count += 1

# 출석률 계산
attendance_rate = attendance_count / (len(record)) * 100

# 결과 출력
print(f"출석률: {attendance_rate:.1f}%")