# 하나는 가리고 하나는 읽기
# 1. 지역 변수 값 반환 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def label() -> str:
    """
    지역 변수 값을 반환

    Args:
        prefix (str): 지역 변수
        inner_prefix (str): prefix의 값

    Globals:
        text (str): 문자
    
    Returns:
        str: 변수값 출력
    """
    prefix = inner_prefix
    return prefix + text

# 정보 입력
parts = input().split()
prefix = parts[0]
text = parts[1]
inner_prefix = parts[2]

# 함수 호출 및 출력
print(label())
print(prefix)
