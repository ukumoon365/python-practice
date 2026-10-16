# 학생 삭제
# 1. 이름 입력
# 2. 입력 받은 이름 딕셔너리에서 삭제
# 3. 딕셔너리 순회
#   1) 각 항목 출력

# 학생 점수 정보 딕셔너리
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}

# 이름 입력
name = input()

# 입력 받은 학생을 딕셔너리에서 삭제
del scores[name]

# 딕셔너리 순회
for name, score in scores.items():
    print(f"{name}: {score}") # 항목 출력