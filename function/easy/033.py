# 지역변수가 전역변수를 가린다
# 1. 지역 변수 반환 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력


def paint() -> str:
    """
    지역 변수 반환 함수
    
    Returns:
        str: 지역변수 
    """
    color = inner
    return  color

# 정보 입력
parts = input().split()
color = parts[0]
inner = parts[1]

# paint 함수 반환값 및 전역 변수 color 출력
print(paint())
print(color)