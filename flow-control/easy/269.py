# 리스트에서 K 이상인 첫 원소 찾기
# 1. 정수 입력
# 2. 리스트 순회 (인덱스, 값)
#   1) k값 이상의 수 발견 즉시 반복 종료
# 3. 결과 출력

# 숫자 리스트
nums = [4, 7, 15, 3, 22, 9]

# 정수 입력
k = int(input())

# 플래그 변수 초기화
found = False

# 리스트 순회 for문
for i, nums_element in enumerate(nums):  
    # k이상 수 판별 if문
    if nums_element >= k:
        found = True    # 플래그 변수값 수정
        break 

# 결과 출력
if found:
    print("위치:", i)         
    print("값:", nums_element)
else:
    print("찾지 못했습니다")