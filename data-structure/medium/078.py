# 두 dict 병합
# 1. 시나리오 번호 입력
# 2. 두 딕셔너리 병합
# 3. 딕셔너리 순회
# 4. 결과 출력

# 두개의 딕셔너리 집합
main_sets = [
    {"수학": 80, "영어": 75, "과학": 90},
    {"A": 1, "B": 2},
    {"X": 10, "Y": 20},
]
update_sets = [
    {"영어": 88, "역사": 70},
    {"C": 3, "D": 4},
    {},
]

# 시나리오 번호 입력
t = int(input())
main = main_sets[t]
update_data = update_sets[t]

# 업데이트 데이터를 업데이트 / 중복 값은 덮어 쓰기 / 새 키 추가
main.update(update_data)

# 딕셔너리 순회 / 결과 출력
for name, value in main.items():
    print(f"{name}: {value}")