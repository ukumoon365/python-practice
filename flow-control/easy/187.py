# 가격표 출력
# 1. 단가, 수량범위 입력
# 2. 1부터 수량범위까지 반복
# 3. 가격표 출력

# 단가, 수량범위 입력
price = int(input())
n = int(input())

# 1부터 n번 반복 for문
for i in range(1, n + 1):
    print(f"{i} x {price} = {i * price}")