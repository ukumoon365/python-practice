# 제곱 Lookup Table
# 1. 정수 입력
# 2. 제곱 딕셔너리 컴프리헨션
# 3. 딕셔너리 순회 
# 4. 결과 출력

# 정수 입력
n = int(input())

# 제곱 lookup table 컴프리헨션 
square_table = {x: x*x for x in range(1, n + 1)}

# 딕셔너리 순회
for value, result in square_table.items():
    # 결과 출력
    print(f"{value}: {result}") 