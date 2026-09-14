# 홀짝 판별기
"""
1. 정수 입력
2. if문을 통해 홀짝 판별
3. 결과 출력
"""
# 정수 입력
num = int(input())

# 숫자(num)를 2로 나누어 나머지로 홀수,짝수 판별
if num % 2 == 0:
    result = "짝수"
else:
    result = "홀수"

# 결과 출력
print (f"{num}은(는) {result}입니다")