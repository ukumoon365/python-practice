# 문자열의 각 글자 대문자 리스트
# 1. 문자열 입력
# 2. 각 글자를 대문자로 변환 후 리스트에 저장
# 3. 한글자 씩 공백 구분으로 출력

# 문자열 입력
s = input()

# 대문자 리스트
str_upper = [char.upper() for char in s]    # .upper는 숫자/기호에 영향을 주지 않음 -> 문자만 대문자 변환

# 결과 출력
print(*str_upper)