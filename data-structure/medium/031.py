# 양 끝 K개씩 잘라내기
# 1. k값 입력
# 2. 슬라이싱을 사용하여 양 끝 k개씩 잘라내기
# 3. 결과 출력

# 데이터 리스트
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# k값 입력
k = int(input())

# 만약 k=0일 경우 빈 슬라이스가 되기 때문에 if 문으로 처리
if k == 0:
    print(" ".join(map(str, data)))
else:
    # 슬라이싱을 사용 [k:]로 앞에 k개 제거 / [:-k]로 뒤에 k개 제거 -> [k:-k]
    print(" ".join(map(str, data[k:-k])))
