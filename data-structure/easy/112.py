# f-string 정렬 포맷
# 1. 이름, 정렬 옵션 입력
# 2. 정렬 포맷
# 3. 결과 출력

# 이름, 옵션 입력
name = input()
opt = input()

# f-string으로 opt 값에 맞게 정렬 if문 / 결과 출력
if opt == "L": 
    print(f"|{name:<10}|")
elif opt == "R":
    print(f"|{name:>10}|")
elif opt == "C":
    print(f"|{name:^10}|")