# ReLU 변환
# 1. 시나리오 번호 입력
# 2. 해당 시나리오의 리스트 순회
#    만약 음수이면 0으로 양수와 0은 그대로 출력

# 3차원 리스트
data_sets = [
    [-3, 5, -1, 0, 4, -7, 2, -10, 8],
    [-1, -5, -10],
    [10, 20, 30],
]

# 시나리오 번호 입력
t = int(input())
data = data_sets[t]

# ReLU 변환 컴프리헨션
change_relu = [num if num > 0 else 0 for num in data]

# 결과 출력
print(*change_relu)