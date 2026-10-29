# 순위 나열
# 1. 순서 나열 함수 정의
# 2. 정보 입력
# 3. 함수 호출 및 출력

def ranking(category: str, *names: str) -> str:
    """
    순서 나열 함수

    Args:
        category (str): 카테고리
        *names (str): 임의 개수의 이름
    
    Returns:
        str: 순위 나열 결과 
    """
    return f"{category}: {' > '.join(names)}"

# 정보 입력
raw = input().split()
category = raw[0]
names = raw[1:]

# 함수 호출 및 출력
print(ranking(category, *names))
