# 각 원소 제곱하기
# 1. 시나리오 번호 입력
# 2. 해당 리스트를 컴프리헨션을 이용하여 각 원소를 제곱한 새 리스트 생성
# 3. 결과 출력

# 3차원 리스트
data_sets = [
    [1, 2, 3, 4, 5, 6, 7],
    [10, 20, 30],
    [0],
]

# 시나리오 번호 입력
t = int(input())
nums = data_sets[t]

# 각 원소 제곱한 리스트 생성
square = [num ** 2 for num in nums]

# 결과 출력
print(" ".join(map(str, square)))