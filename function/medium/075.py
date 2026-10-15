# 모음 개수 세기 함수
# 1. 모음 개수 세기 함수 정의
# 2. 문자열 입력
# 3. 함수 호출 및 출력

def count_vowels(s:str) -> int:
    """
    모음 개수 카운트 함수

    Args:
        s (str): 입력 받은 문자열

    Returns:
        int: 모음 개수 카운트
    """

    vowels_set = ("a", "e", "i", "o", "u")  # 모음 집합
    count = 0   # 카운트 변수


    # 문자열 순회
    for char in s:
        # 모음 포함 검사 if문
        if char in vowels_set:
            count += 1
    
    return count

# 문자열 입력
s = input()

# 결과 출력
print(count_vowels(s))