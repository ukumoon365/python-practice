# set에서 원소 제거
# 1. 원소 입력
# 2. 해당 원소 제거
# 3. set 정렬
# 4. 결과 출력

# set
fruits = {"apple", "banana", "cherry", "date", "fig"}

# 제거할 원소 입력
item = input()

# 입력 받은 요소 제거
fruits.discard(item)
# 집합 정렬
sorted_fruits = sorted(fruits)

# 결과 출력
print(" ".join(sorted_fruits))