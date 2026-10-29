# 비밀번호 생성기
# 1. 정수 입력
# 2. 1~n 반복 
#   1) 홀수번째 알파벳 출력
#   2) 짝수번째 숫자 출력

# 정수 입력
n = int(input())

# 인덱스 변수 초기화
num_index = 1
alpha_index = 0

# 1~n반복 for문
for password_len in range(1, n + 1):
    # 홀수/ 짝수 판별 if문
    if password_len % 2 == 0:
        print(num_index % 10, end="")  # % 10으로 9 이후 0 자동 순환
        num_index += 1
    else:
        print(chr(97 + alpha_index % 26), end="")  # % 26으로 z 이후 a 자동 순환
        alpha_index += 1