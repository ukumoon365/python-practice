# 매개변수가 전역변수를 가린다
# 인사 반환 함수 정의
# 정보 입력
# 함수 호출 및 출력

# 인사를 반환하는 함수 정의
def greet(name: str) -> str:
    """
    인사말을 반환

    Args:
        name (str):이름

    Returns:
        str: 인사말
    
    """
    return f"안녕, {name}"

# 정보 입력
parts = input().split()
name = parts[0]
guest = parts[1]

# 결과 출력
print(greet(guest))
print(name)