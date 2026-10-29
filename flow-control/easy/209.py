# 배열 출력
# 1. 정수 입력
# 2. 1~n*n까지 n간격으로 반복
#   1) 행과 열 출력

# 정수 입력
n = int(input())

for row_start in range(1, n * n, n):
    # join을 사용해 마지막 탭 없이 탭 구분 출력
    print('\t'.join(str(row_start + col) for col in range(n)))