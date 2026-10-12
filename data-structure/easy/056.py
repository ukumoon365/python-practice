# 좌표 tuple에서 x, y 추출
# 1. x, y 값을 입력
# 2. 튜플을 이용하여 두 값을 묶음
# 3. 결과 출력

# x,y 값 입력
x = int(input())
y = int(input())

# tuple로 두 값을 묶음
point = (x, y)

# 결과 출력
print(f"x: {point[0]}")
print(f"y: {point[1]}")
