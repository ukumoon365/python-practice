# 숫자 분해
# 1. 3자리 정수 입력
# 2. 각 자리로 분해
# 3. 자리 수의 합과 곱 계산
# 4. 결과 출력

# 정수 입력
num = int(input())

# 각 자리 분해
num_digit_one = num % 10 
num //= 10
num_digit_ten = num % 10
num_digit_hundred = num // 10

# 세자리 합 계산
total_num_sum = num_digit_hundred + num_digit_ten + num_digit_one
# 세자리 곱 계산
total_num_multiplication = num_digit_hundred * num_digit_ten * num_digit_one

# 결과 출력
print(f"백의자리: {num_digit_hundred}")
print(f"십의자리: {num_digit_ten}")
print(f"일의자리: {num_digit_one}")
print(f"합: {total_num_sum}")
print(f"곱: {total_num_multiplication}")