# 슬라이스로 원본 보존 복사
# 1. 시나리오 번호 입력
# 2. 슬라이싱을 이용하여 사본 생성 / 정렬
# 3. 결과 출력

# 3차원 리스트
data_sets = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 3, 1],
    [7],
]

# 시나리오 번호 입력
t = int(input())
original = data_sets[t]

# 슬라이싱으로 원본 복사
copy = original[:]
# 정렬
copy.sort()

# 결과 출력
print("원본:"," ".join(map(str, original)))
print("정렬:"," ".join(map(str, copy)))
print("원본:"," ".join(map(str, original)))