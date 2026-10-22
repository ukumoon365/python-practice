# 배수 판별기
# 1. num과 n을 입력 
# 2. 2부터 n까지 반복
#   1) 각각의 배수인지 판별
#   2) 결과 출력

# 정수 입력
num = int(input())
n = int(input())

# 2부터 n까지 반복 for문
for i in range(2, n + 1):
    # 배수 판별 if문
    if num % i == 0:
        print(f"{i}의 배수입니다.")
    else:
        print(f"{i}의 배수가 아닙니다.")
