# 학생 n명 등록
# 1. 학생 인원 수 입력
# 2. 인원 수 만큼 반복
#   1) 이름, 성적 입력
#   2) 이름과 성적 딕셔너리 저장
# 3. 딕셔너리 순회
#   1) 결과 출력

# 학생 인원 수 입력
n = int(input())

students_info = {}  # 학생 성적 정보 딕셔너리

# 인원수 만큼 반복 for문
for _ in range(n):
    # 이름, 성적 입력
    name = input()
    score = input()

    # 딕셔너리에 저장
    students_info[name] = score

# 딕셔너리 순회 및 결과 출력
for name, score in students_info.items():
    print(f"{name}: {score}")
    