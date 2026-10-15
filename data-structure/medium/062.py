# 학생 정보 조회
# 1. 이름 입력
# 2. 리스트 순회
#   1) 해당 학생 존재 여부 판별
# 3. 결과 출력

# 학생 정보 튜플 리스트
students = [
    ("윤서", 85),
    ("지우", 92),
    ("민준", 65),
    ("서윤", 78),
    ("도윤", 95),
]

# 이름 입력
target = input()

# 플래그 변수 초기화
found = False

# 리스트 순회 for문
for name, score in students:
    # 학생 존재 여부 판별 if문
    if name == target:
        found = True
        break

# 결과 출력
if found:
    print(f"점수: {score}")
else:
    print("학생 없음")