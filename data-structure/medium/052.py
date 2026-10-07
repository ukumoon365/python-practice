# 라벨 인코딩
# 1. 정수 입력
# 2. 딕셔너리 컴프리헨션
# 3. 결과 출력

# 라벨 리스트 
labels = ["cat", "dog", "bird", "fish", "lion"]

# 정수 입력
n = int(input())

# 컴프리헨션으로 이름: 인덱스 (n까지)의 딕셔너리 생성
labels_dict = {name: index for index, name in enumerate(labels[:n])}

# 딕셔너리를 순회 for문
for name, index in labels_dict.items():
    # 결과 출력
    print(f"{name}: {index}")
