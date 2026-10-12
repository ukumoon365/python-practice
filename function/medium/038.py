# 여러 전역변수 읽기
# 1. 전역 변수를 읽고 값을 반환하는 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def describe() -> str :
    """
    전역변수 name, age를 읽고 값을 반환 
    
    Globals:
        name (str): 이름
        age (str): 나이

    Return
        str: "{name}({age})"
    """
    return f"{name}({age})"

# 정보 입력
parts = input().split()
name = parts[0]
age = parts[1]

# 결과 출력
print(describe())