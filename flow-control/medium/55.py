# 짝수만 누적
# 1. 5개의 정수를 입력 받는다
# 2. 홀수는 건너 뛰고 짝수만 누적 합계 
# 3. 결과 출력

# 반복문을 5번 반복
for _ in range(5):
    num = int(input())  # 정수 입력
    if num % 2 != 0:    # 홀수 
        print("홀수는 건너뜁니다")
        continue        # 건너 뛰기
    total += num        # 짝수만 누적 합계

# 결과 출력
print(f"짝수 합계: {total}")