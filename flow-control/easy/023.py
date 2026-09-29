# 혈액형 성격
# 1. 혈액형 입력
# 2. 혈액형에 따라 성격 구분
# 3. 결과 출력

blood = input()

#혈액형에 따른 성격 구분 if문
if blood == "AB": #순차 진행이기에 AB먼저 검사
    personality = "이성적이고 독창적인 성격"
elif blood == "A":
    personality = "꼼꼼하고 신중한 성격"
elif blood == "B":
    personality = "자유롭고 창의적인 성격"
elif blood == "O":
    personality = "사교적이고 리더십이 강한 성격"
else: 
    personality = ""

# 결과 출력
if personality:
    print(f"혈액형: {blood}형")
    print(f"성격: {personality}")
else:
    print("잘못된 입력입니다.")