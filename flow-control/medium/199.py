# 단어 뒤집기
# 1. 문자열 입력
# 2. 문자열 순회
#    순서대로 문자열을 저장 / 공백이 나오면 저장한 문자열 뒤집기 -> 결과에 추가 /
#    문자열의 끝의 마지막 단어도 뒤집어 추가
# 3. 결과 출력

# 문자열 입력
s = input()

# 변수 초기화
result = ""
word = ""

# 문자열 순회 for문
for char in s:
    # 구분자 판별 if문
    if char == " ":
        result += word[::-1] + " "
        word = ""
    else:
        word += char  
          
# 문자열 마지막 단어도 뒤집기     
result += word[::-1]

# 결과 출력
print(result)