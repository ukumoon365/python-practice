# 2D 좌표 생성
# 1. 행 수와 열 수를 입력
# 2. 이중 for 컴프리핸션으로 좌표 생성
# 3. 결과 출력

# 행, 열 입력
r = int(input())
c = int(input())

# 이중 for문 컴프리헨션 / 출력
print(" ".join(f"({x},{y})" for x in range(r) for y in range(c)))