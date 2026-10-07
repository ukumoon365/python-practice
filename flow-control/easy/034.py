# 약수 구하기
# 1. 정수 입력
# 2. 1~N까지 나누어 약수를 구한다 
# 3. 결과 출력

# 정수 입력
n = int(input())

print(f"{n}의 약수:",end=" ")  # "N의 약수:" 반복 방지

for number in range(1, n + 1):
    if n % number == 0:  # 1~n까지 나누어 약수 구하기
        print(number,end=" ")