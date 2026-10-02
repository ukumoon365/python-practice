# 짝수만 추출
# 1. 시나리오 번호 입력
# 2. 해당 리스트의 짝수만 추출
#    리스트 컴프리헨션에 반복문과 if문 사용
# 3. 결과 출력

# 3차원 리스트
data_sets = [
    [1, 4, 7, 2, 9, 6, 3, 8, 10, 5],
    [1, 2, 3, 4, 5],
    [1, 3, 5, 7, 9],
]

# 시나리오 번호 입력
t = int(input())
data = data_sets[t]

# 짝수만 추출 컴프리헨션
even_data = [num for num in data if num % 2 == 0]

# 결과 출력
print(" ".join(str(result) for result in even_data))