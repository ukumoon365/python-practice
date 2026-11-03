# Unpacking
## List, Str, range(객체), Dictionary, Set
```text

    1) 기본 unpacking (언패킹)
        bar = (1, 2)
        a, b = bar # a = 1, b = 2
    2) 변수 swap (임시 변수 ❌)
        a, b = 1, 2
        a, b = b, a
    3) 함수 다중 반환
        def funtion(a, b):
        retrun a, b
        c, d = funtion(a, b) # a = c, d = b
    4) *로 나머지 묶기
        a, *b = [1, 2, 3, 4] # a = 1, b = [2, 3, 4]
        a,*b , c = [1, 2, 3, 4] # a = 1, b = [2, 3], c = 4 
```
