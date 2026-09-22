# 내장 함수는 Built-in 범위에서
# 1. 전역변수 길이 반환 함수 정의
# 2. 문자열 입력
# 3. 함수 호출 및 출력
 
def count() -> int:
    """ 
    전역변수 길이 반환 함수

    Returns:
        int: 전역변수 word의 길이
    """
    return len(word)

# 문자열 입력
word = input()

# 함수 호출 및 출력
print(count())