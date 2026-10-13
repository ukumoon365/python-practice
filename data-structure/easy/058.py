# 두 변수 swap
# 1. 두개의 정수 입력
# 2. 교환 전 출력
# 3. 언패킹을 사용하여 두 값을 바꿈
# 4. 결과 출력

# 두개의 정수 입력
a = int(input())
b = int(input())

# 교환 전 출력
print(f"교환 전: a={a} b={b}")

# 언패킹으로 변수 swap
a, b = b, a

# 결과 출력
print(f"교환 후: a={a} b={b}")