# 특정 문자 찾기
"""
1. 글자 수 만큼 반복
   target의 글자가 있을 경우 -> found = True    
2. 끝까지 찾지 못할 경우 -> found = False      
"""

# 문자열 초기화
text = "hello python"

# 타켓 값 초기화
target = "p"

# found 값 초기화
found = False                   
for i in range(len(text)):
    if (text)[i] == target:
        found = True    # found 값 True = 찾음
        break   # 반복 종료

if found:
    print(f"'{target}'을(를) {i}번째 위치에서 찾았습니다!")
else:   # found == false  / 찾지 못했을 경우
    print("찾지 못했습니다")