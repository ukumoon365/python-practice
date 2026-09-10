# Variable (변수)
```text
데이터를 저장 하는 공간
    - 지정 이름을 통해 데이터를 읽고 저장 📖
    - 데이터를 다루기 위한 기본 요소 ✅

사용 목적
    - 값에 이름을 붙여 저장 / 읽기 or 수정

변수 분석의 4가지 관점
    ✔️Variable Declaration (변수 선언)
        ○ 변수는 데이터를 저장하고 참조하기 위한 이름
        ○ 『이름 = 값』 형태로 작성
            § 의미가 있는 이름으로 작성
            § Python에선 snake_case 사용 권장
            § 영문자, 숫자, "_" 사용 
            § 숫자 시작, 공백 ❌
            § 대소문자 구분
            § 예약어 (if, while ….) ❌
    
    ✔️Data Types of Variables (변수 자료형)
        ○ 서로 다른 종류의 데이터를 저장 할 수 있다
        ○ 기본 자료형 Type
            § Number (숫자)
                □ Integer (정수)
                □ Float (실수)
            § String (문자형)
                □ " ", ' '
            § Boolean (불린형)
                □ True
                □ False
                    ® 모든 값의 Truthy, Falsy
                        - bool(0) # False
                        - bool(1) # True
                        - bool("") # False
                        - bool("hello") # True
                        - bool([]) # False
                        - bool([1, 2]) # True
                    ® None 값은 False
                    
        ○ 기본 자료형 변환 함수
            § int() : 정수
            § Float() : 실수
                □ int(), float()은 숫자 형태 문자열만 숫자 변환 가능
                □ Float -> integer로 변환시 소수점은 이하는 버려진다
            § str() : 문자
                □ 기본 input()은 문자열 -> 따라서 연산이 필요할 경우 int() or float()으로 변환 필요
                □ 문자열 상태에서 + -> 이어붙이기 * -> 반복
                
    ✔️Variable Scope (변수 범위)
        ○ 해당 변수를 사용할 수 있는 코드 영역
    ✔️Lifecycle of a Variable (변수의 생명주기)
        ○ 변수의 생성 및 사용, 소멸의 과정
``` 