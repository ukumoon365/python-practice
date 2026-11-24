# 콜라츠 추측
# 1. 정수 입력
# 2. n이 1이 될때까지 반복
#       1) 짝수,홀수 판별
#       2) 횟수 카운트
# 3. 결과 출력

# 카운트 변수 초기화
count = 0

# while 반복문
while n > 1:
    # 정수 출력
    print(n)
    # 짝수, 홀수 판별 if문
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    # 횟수 카운트
    count += 1

# 결과 출력
print(n)
print(f"횟수: {count}")