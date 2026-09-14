# 나만의 파스타 만들기
"""
1. 각 재료의 사용 여부를 입력
2. if문을 통해 재료 추가
3. 결과 출력
"""
# 각 재료의 추가 여부 입력
add_cheese = input()
add_bacon = input()
add_shrimp = input()

# 파스타 변수 초기화
pasta = "파스타"

# 재료 추가 여부에 따라 파스타 제조
if add_cheese == "예":
    pasta += " + 치즈"
if add_bacon == "예":
    pasta += " + 베이컨"
if add_shrimp == "예":
    pasta += " + 새우"

# 결과 출력
print ("나의 파스타:",pasta)