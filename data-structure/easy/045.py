# 모음만 추출
# 1. 문자열 입력
# 2. 문자열 순회 및 소문자 변환 / 모음 확인
# 3. 결과 출력

# 문자열 입력
s = input()

# 문자열 순회 컴프리헨션
vowels = [char for char in s if char.lower() in "aeiou"]    # 문자열을 순회 / 문자를 소문자로 변환 후 모음 확인

# 결과 출력
print("".join(vowels))  # "".join으로 공백 없이 이어 붙여 출력