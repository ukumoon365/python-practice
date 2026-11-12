# f-string 소수점 포맷
# 1. 실수, 소수점 자릿수 입력
# 2. 소수점 포맷 및 결과 출력

# 실수, 소수점 자릿수 입력
value = float(input())
n = int(input())

# 결과 출력
print(f"{value:.{n}f}")
