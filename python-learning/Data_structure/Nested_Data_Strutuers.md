## Nested Data Strutuers
```text
여러 자료구조를 중첩으로 사용
    1) List in List
        bar = [ [1,2,3], [4,5,6]]
    2) Dict in List
        bar = {a: [1, 2, 3]}
    3) 🌟 List in Dict
    4) bar = [ {a: 1} ]
        print(a[1][a]) # 1

✔️ 2차원 리스트 (행렬)
```
![alt text](<../images/Nested Data Strutuers_matrix.png>)
```
⚠️ [[0]*3] * 3 -> 같은 행 공유
    ➡️ [[0] * 3 for _ in range(3)] 

✔️ 처리 패턴
```
![alt text](<../images/Nested Data Strutuers_pattern.png>)
## Copy
```text
✔️ 복사
    - shallow
    바깥은 새것 , 안쪽은 공유
    bar = foo.copy / foo[:] / list(foo)
    
    - deep
    바깥, 안쪽 새것
    bar = copy.deepcopy(foo)
```