# 출석 체크
"""
1. 출석할 인원 수 입력
2. 인원수 만큼 반복
   이름 입력 -> 리스트에 추가
3. 결과 출력
"""
# 인원 수 입력
n = int(input())

# 리스트 생성
attendance = []

for _ in range(n):
    name = input()
    attendance.append(name)

print(f"출석 {n}명")
print(f"명단: {' '.join(attendance)}")