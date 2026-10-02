# 양수만 추출
# 1. 시나리오 번호을 입력
# 2. 해당 시나리오의 양수만 추출
#    컴프리션헨션에 반복문 및 if문 사용
# 3. 결과 출력

# 3차원 리스트
data_sets = [
    [3, -1, 0, 7, -5, 2, -8, 4],
    [-3, 10, -5, 20, 0],
    [-1, -2, 0, -3],
]

# 시나리오 번호 입력
t = int(input())
data = data_sets[t]

# 양수만 추출 컴프리션헨션 
data_num = [num for num in data if num > 0]

# 결과 출력
print(" ".join(map(str, data_num)))