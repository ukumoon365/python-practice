# Train/Validation 데이터 분할
"""
1. 데이터 비율 p를 입력
2. 분할 위치를 계산
3. 앞에서부터 tarin과 val 두 부분으로 분할
4. 결과 출력
"""
# 데이터
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 데이터 비율
p = int(input())

# 위치 계산
split_index = len(data) * p // 100

# 결과 출력
print("train:"," ".join(map(str, data[:split_index])))
print("val:"," ".join(map(str, data[split_index:])))