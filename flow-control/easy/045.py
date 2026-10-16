# 숫자 자릿수 세기
# 1. 정수 입력
# 2. 자릿수가 1이 될 때까지 반복
#   1) 자릿수 빼기
#   2) 자릿수 카운트
# 3. 결과 출력

# 정수 입력
num = int(input())
count = 0 # 카운트 변수 초기화
original_number = num  # 원본 값 보관

# 자릿수가 1이 될 때까지 반복 while문
while num > 0:
    num //= 10  #  10씩 나누어 자릿수 빼기
    count += 1  # 카운팅

# 결과 출력
print(f"{original_number}은(는) {count}자리 수입니다.")