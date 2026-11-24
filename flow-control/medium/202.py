# 진법 변환
# 1. 정수 입력
# 2. n이 0이 될 때까지 반복 
#    8로 나눈 값의 나머지는 리스트에 저장
#    8로 나눈 값의 몫은 변수로 저장
# 3. 리스트를 역순으로 출력

# 정수 입력
n = int(input())

# 리스트 변수 초기화
result = []

# 0이상 정수 판별 if문
if n == 0:
    result.append(0)
else:
    while n > 0:
        # 리스트 항목 추가
        result.append(n % 8)
        n //= 8 

# 리스트 역순 정렬
result.reverse()

# 결과 출력
print("".join(map(str, result)))