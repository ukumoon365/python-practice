# 미니 성적 관리
# 1. 5번 반복
#   1) 5명의 점수 입력
# 2. 점수 총합, 최고점, 평균 계산
# 3. 결과 출력

# 총합 변수 초기화
total = 0
# 최고점 변수 초기화
best = 0

# 5번 반복 for문
for scores in range(5):
    # 점수 입력
    score = int(input())
    
    total += score      # 총점 누적 계산

    # 최고점 판별 if문
    if best < score:
        best = score    # 최고점 갱신

# 평균 값 계산
average = total / 5

# 결과 출력
print(f"평균: {average}")
print(f"최고점: {best}")
