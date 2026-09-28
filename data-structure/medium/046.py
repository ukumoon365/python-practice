# Min-Max 정규화
# 1. 양수 2 이상, 8 이하를 입력
# 2. 정규화 계산
# 3. 결과 출력 (소수점 둘째 자리까지)

# 데이터 리스트
data = [10, 20, 30, 40, 50, 60, 70, 80]

# 양수 입력
n = int(input())

# 슬라이싱 값 
slied = data[:n]

# n번째값 까지의 min, max 값 구하기 
min_val = min(slied)
max_val = max(slied)

# n번째 리스트 요소까지 정규화 계산 
# 소수점 둘째자리까지만 리스트에 저장
result = [f"{(val - min_val) / (max_val - min_val):.2f}" for val in slied]

# 언패킹으로 공백 구분 출력
print(*result)