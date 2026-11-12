# set 순회 + 조건 필터
# 1. cutoff 입력
# 2. set 순회 및 조건 필터에 맞는 리스트 생성
# 3. 결과 출력

# 정수 set
numbers = {1, 5, 3, 8, 2, 10, 7, 4}

# cutoff 입력
cutoff = int(input())

# 컴프리헨션 / 조건 필터에 맞는 값 추가
cutoff_over_list = [value for value in numbers if value >= cutoff]

# 리스트 정렬
cutoff_over_list.sort()

# 결과 출력 / 언패킹으로 값만 출력
print(*cutoff_over_list)