# Magic Method
``` text
 ✔️ 매직 메서드
파이썬 인터프리터에 정의 되어 있는 메서드
ex) +연산자를 만나면 -> __add__ 메소드 호출

✅ 매직 메서드 == dunder(던더) 메서드

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        print(self.x, self.y)
        return Point((self.x + other.x), (self.y + other.y))
# __init__ 메서드 호출 -> (10, 20) / (20, 30)은 각각 인스턴스 self에 등록
dot1 = Point(10, 20) 
dot2 = Point(20, 30)
dot3 = dot1 + dot2 # __add__ 메서드 호출 ⚠️ + 연산 ❌  / __add__ 메서드 호출 ⭕
print(dot3.x, dot3.y)
# 10 20
# 30 50

✔️ 부호와 메서드 연관표
a + b	a.__add__(b)
a * 3	a.__mul__(3)
a == b	a.__eq__(b)
len(a)	a.__len__()
a[0]	a.__getitem__(0)
x in a	a.__contains__(x)
print(a), str(a)	a.__str__()
a()	a.__call__()
Car() (인스턴스 생성)	Car.__new__(Car) 다음 __init__(self)

✔️ 주요 메서드
	1) 생성자, 소멸자
	- __init__(self, ....): 객체 생성시 호출되는 생성자 메서드
	- __del__(self): 객체가 소멸될 때 호출되는 소멸자 메서드

	2) 문자열 표현
	- __str__(self): str()함수 출력 결과와 같음 / print로 출력되는 결과도 동일 ⚠️ 공식적 ❌, 좋게 안보이는 문자열 표현 반환 
			✅ 공식적인 표현은 repr
	- __repr__(self): repr()함수 출력 결과와 같음 / ⭐ 공식적인 문자열 반환
	
	3) 산술 연산
	- __add__(self) : 덧셈
	- __sub__(self):  뺄셈
	- __mul__(self, other): 곱셈
	- __truediv__(self, other): 나눗셈(/)
	
	4) 비교 연산
	- __eq__(self, other): ==
	- __ne__(self, other): !=
	
	5) 컨테니어 타입 연산
	- __len__(self): len()와 같음
	- __getitem__(self, key): 인덱싱 연산 object[key]와 같음
	- __setitem__(self, key, value): 항목 할당
	- __contains__(self, value): in 연산자
	
	6) 호출 가능 객체
	- __call__(self, ...): 객체를 함수처럼 호출
```