# 마지막 등록 취소
# 1. 시나리오 번호 입력
# 2. .pop() 메서드를 사용하여 마지막 등록 취소
# 3. 결과 출력

# 3개의 시나리오
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]

# 시나리오 번호 입력
t = int(input())

# 해당 시나리오 리스트
applicants = data_sets[t]

print(f"취소된 사람: {applicants.pop()}")   # .pop()으로 마지막 원소 제거 후 반환
print(f"남은 명단: {' '.join(applicants)}") # 마지막 원소가 제거된 리스트 출력