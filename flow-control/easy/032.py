# 구구단 출력
# 1. 단 수 입력
# 2. 반복문으로 구구단 계산 
# 3. 결과 출력

# 단입력
dan = int(input())

# 구구단 반복 for문
for a in range (1,10):
    result = dan * a
    print(f"{dan} x {a} = {result}")
    