# 파일 저장 판정
# 1. 파일 이름, 확장자 입력
# 2. 이름 입력 여부 판별
#   1) 확장자 판별
# 결과 출력

# 파일 이름 입력
filename = input()
# 파일 확장자 입력
extension = input()

# 이름 입력 여부 판별 if문/ 결과 출력
if filename:
    # 확장자 판별 if문 / 결과 출력
    if extension == "txt":
        print("텍스트 파일 저장")
    else:
        print("지원되지 않는 형식")
else:
    print("파일명을 입력하세요")