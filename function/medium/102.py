# 자기소개
# 1. 자기 소개 반환 함수
# 2. 정보 입력
# 3. 함수 호출 및 출력
def introduce(name: str, age: str = "20", city: str = "서울") -> str:
    """
    자기소개 함수

    Args:
        name (str): 이름
        age (int): 나이 / 기본 20
        city (str): 지역 / 기본 "서울"

    Returns:
        str: 이름/나이/지역 반환
    """

    return f"{name}/{age}/{city}"

# 정보 입력
parts = input().split()
 
# 결과 출력
if len(parts) == 1:
    print(introduce(parts[0]))
elif len(parts) == 2:
    print(introduce(parts[0], int(parts[1])))
else:
    print(introduce(parts[0], int(parts[1]), parts[2]))