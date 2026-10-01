# 사각형 테두리
# 1. 줄 수 입력
# 2. 사각형 모양 테두리 출력 반복문

# 줄 수 입력
n = int(input())

# 사각형 테두리 "*" 출력 for문
for row in range(n):   # 줄 세우기
    # 윗면, 아랫면 if문
    if row == 0 or row == n - 1:
        print("*" * n)   # 별 그리기 
    else:
        print("*" + " " * (n - 2) + "*")   # 안쪽은 공백 테두리에만 별 찍기