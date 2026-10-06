# 양수만 제곱
# 1. 시나리오 번호 입력
# 2. 해당 리스트의 양수만 제곱하여 출력
#    리스트 컴프리헨션, if문, 반복문 

# 3차원 리스트
data_sets = [
    [3, -1, 0, 7, -5, 2, -8, 4],
    [10, -5, 20, 0],
    [-1, -2, -3],
]

# 시나리오 번호 입력
t = int(input())
data = data_sets[t]

# 양수만 제곱하는 리스트 컴프리헨션
positive_square = [num ** 2 for num in data if num > 0]

# 결과 출력
print(" ".join(str(num) for num in positive_square))