# 구구단 범위 출력
# 1. 시작단 , 끝단 입력
# 2. 시작단부터 끝단 까지 반복
#    각 단 --- N단 --- 으로 시작
#    1) 구구단 출력

# 시작단 , 끝단 입력
start = int(input())
end = int(input())

# 시작단부터 끝단까지 반복 for문
for i in range(start, end + 1):
    print(f"--- {i}단 ---") # 단 출력
    
    # 구구단 계산 반복 for문
    for j in range(1, 10):
        # 결과 출력
        print(f"{i} x {j} = {i * j}")