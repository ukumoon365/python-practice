# ROT13 암호화
# 1. 문자열 입력
# 2. 문자열 순회
#    1) ROT13 암호화
# 3. 결과 출력

# 문자열 입력
s = input()
# 결과값 변수 초기화
result = ""

# 문자열 순회
for char in s:
    if char.isupper():
        base = ord("A")
    elif char.islower():
        base = ord("a")
    else:   # 알파벳이 아닌 문자는 바로 추가
        result += char
        continue
    change_char = (ord(char) - base + 13) % 26 + base
    result += chr(change_char)

# 결과 출력
print(result)