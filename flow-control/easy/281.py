# 등차수열 출력
start = int(input())
stop = int(input())
step = int(input())

# 1. 시작값, 끝값, 간격을 각각 입력
# 2. 시작, 끝값, 간격에 맞춰 순회
#   1) 인덱스 출력

# 시작값, 끝값, 간격을 각각 입력
start = int(input())
stop = int(input())
step = int(input())

# 시작, 끝값, 간격에 맞춰 순회 for문
for i in range(start, stop, step):
    # 결과 출력
    print(i,end=" ")