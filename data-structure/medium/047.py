# 평균 빼기
# 1. 양의 정수 1 이상 5 이하 값을 입력
# 2. n번째까지의 정수 값에서 평균을 뺀 값을 리스트에 저장
# 3. 결과 출력

# 데이터 리스트
data = [10, 20, 30, 40, 50]

# 양의 정수 입력
n = int(input())

# 슬라이싱 값
sliced_data = data[:n]

# 평균 값
average = sum(sliced_data) // n

# 결과 출력 / 언패킹으로 공백 구분 출력
print(*[(x - average) for x in sliced_data])