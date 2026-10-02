# 알파벳 삼각형
# 1. 줄 수 입력
# 2. 알파벳 삼각형 모양 출력 반복문
# 3. 결과 출력

# 줄 수 입력
n = int(input())

# 알파벳 삼각형 모양 출력 for문
for i in range(1, n + 1):   # 줄 세우기
    alphabet_line = "" . join(str(chr(65 + a)) for a in range(i)) 
    print(alphabet_line)   # 알파벳 출력

