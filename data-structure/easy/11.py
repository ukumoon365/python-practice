# 점수 오름차순 정렬
# 1. 시나리오 입력
# 2. 선택된 리스트를 오름차순으로 정렬 후 변수 저장
# 3. 결과출력

# 3개의 시나리오
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]

# 시나리오 번호 입력
t = int(input())

# 해당 시나리오 
scores = data_sets[t]

# 오름차순 정렬
sort_list = sorted(scores)
# 결과 출력
print(" ".join(map(str, sort_list)))