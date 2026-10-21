# 별 사각형
# 1. 가로,세로를 입력
# 2. 세로 수 만큼 반복
#   1) 넓이 값 만큼 별 출력

# 가로, 세로 값 입력
width = int(input())
height = int(input())

# 세로 수 만큼 반복 for문
for i in range(height):
    # 넓이 값 만큼 별 출력
    print("*" * width)