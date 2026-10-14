# dict의 key로 tuple 사용
# 1. 좌표값 입력
# 2. 좌표 튜플화
# 3. 좌표 존재 여부 확인
# 4. 결과 출력

# 좌표 딕셔너리
positions = {
    (0, 0): 'A',
    (0, 1): 'B',
    (1, 0): 'C',
    (2, 3): 'X',
    (4, 4): 'GOAL',
}

# 좌표값 입력
x = int(input())
y = int(input())

# 입력 받은 값 좌표화 (튜플)
coordinate = (x, y)

# 좌표 존재여부 확인 / 결과 출력
if coordinate in positions:
    print(positions[coordinate])
else:
    print("없음")