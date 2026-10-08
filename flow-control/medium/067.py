# 곱셈표
# 1. 정수 입력
# 2. 헤더 출력
# 3. 구분선 출력
# 4. 곱셈 결과 출력 

# 정수 입력
n = int(input())


# 헤더
print("X", end="\t")
# n번 반복 for문
for col_num in range(1, n + 1):
    print(col_num, end="\t")
print()  # 줄 바꿈

# 구분선
print("-" * 30)

# n번 반복 for문
for i in range(1, n + 1):
    print(i, end="\t")
    # 곱셈 계산 및 출력 for문
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print() # 줄 바꿈