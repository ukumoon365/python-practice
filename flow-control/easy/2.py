# 폭염 경보 출력

# 온도 입력
temperature = int(input())


# 입력 받은 온도가 30도 초과이면 폭염주의보,외출을 자제하세요 출력
if temperature > 30:
    print("폭염주의보")
    print("외출을 자제하세요")