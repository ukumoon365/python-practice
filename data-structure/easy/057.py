# RGB 색상 언패킹
# 1. r,g,b 값을 입력
# 2. 각 값을 튜플로 불변하게 만듬
# 3. 언패킹으로 세 변수로 다시 나눔
# 4. 결과 출력

# r,g,b 값을 입력
r = int(input())
g = int(input())
b = int(input())

# tuple화
color = (r, g, b)

# 언패킹
r, g, b = color

# 결과 출력
print(f"R: {r}")
print(f"G: {g}")
print(f"B: {b}")