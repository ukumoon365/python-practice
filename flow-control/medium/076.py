# 간단한 계산기
# 1. 두개의 실수와 연산자 입력
# 2. 각 연산자에 맞게 계산 
# 3. 결과 출력

# 실수 입력
num1 = float(input())
num2 = float(input())
# 연산자 입력
op = input()

# 연산자 판별 if문
if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:   # 0이 아닌 값
        print(f"{num1} / {num2} = {num1 / num2}")
else:   # 지원하지 않는 연산자
    print("지원하지 않는 연산자입니다.")