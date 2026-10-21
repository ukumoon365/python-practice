# 숫자 카운트
# 1. 정수 입력
# 2. 1 ~ N까지 반복
#    1) 3의 배수, 5의 배수, 공배수 개수 카운트
# 3. 결과 출력

# 정수 입력
n = int(input())

# 각 카운트 변수 초기화
multiple_three = 0
multiple_five = 0
multiple_common = 0

# 1부터 n까지 반복 for문
for i in range(1, n + 1):
    # 배수, 공배수 판별 if문
    if i % 3 == 0 and i % 5 == 0:   # 3,5 공배수
        multiple_common += 1
    if i % 3 == 0:
        multiple_three += 1
    if i % 5 == 0:
        multiple_five += 1

# 결과 출력
print(f"3의 배수: {multiple_three}개")
print(f"5의 배수: {multiple_five}개")
print(f"3과 5의 공배수: {multiple_common}개")

# 계산식으로 푸는 방법
multiple_three = n // 3
multiple_five = n // 5
multiple_common = n // 15   # 3과 5의 최소공배수(15)의 배수 개수
