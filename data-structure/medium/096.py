# 단어 중복 제거 후 정렬 출력
# set 중복 제거 / split 공백 제거/ sorted 정렬

# 결과 출력
print(' '.join(sorted(set(input().split()))))