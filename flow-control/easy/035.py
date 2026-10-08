# 1부터 N까지의 합
# 1. 정수 입력 
# 2. 1~N까지 반복
# 3. 누적합 계산
# 4. 결과 출력

# 정수 입력
n = int(input())

# 누적합 변수 초기화
total = 0  

# n번 반복 for문
for i in range(1, n+1):
    total += i # 누적합 

# 결과 출력
print(f"1부터 {n} 까지의 합: {total}")