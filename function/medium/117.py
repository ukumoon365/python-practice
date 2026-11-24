# 단어들 이어 붙이기
# 1. 단어들 이어 붙이기 함수 정의
# 2. 단어 입력
# 3. 함수 호출 및 출력
def concat_words(*words: str) -> str:
    """
    단어들을 "-"로 이어 붙인 후 반환 하는 함수

    Args:
        *words (str): 임의 개수의 단어들
    
    Returns:
        str: 각 단어들을 "-"으로 이어 붙인 후 반환
    """
    return "-".join(words)

# 단어 입력
words = input().split()

# 결과 출력
print(concat_words(*words))
