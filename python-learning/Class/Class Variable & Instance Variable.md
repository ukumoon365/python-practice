## Class Variable & Instance Variable
```text
 ✔️클래스 변수
    클래스를 통해 만들어진 모든 인스턴스 객체들이 공유하는 변수 값
    ⭐ 클래스가 메모리에 로드될 때 생성
class Car:
    # 클래스 변수의 위치
    max_speed = 300
    max_people = 5

modelx = Car()
modely = Car()

modely.max_speed = 500 # 인스턴스 변수의 값을 조정
print(Car.max_speed)  # 300
print(modelx.max_speed)  # 300
print(modely.max_speed)  # 500 

Car.max_speed = 500 # 클래스 변수의 값으 조정
print(Car.max_speed)  # 500
print(modelx.max_speed)  # 500
print(modely.max_speed)  # 500

⭐ max_speed, max_people 각각의 메모리 영역이 아니라 하나의 메모리 영역을 공유

✔️ 인스턴스 변수
    각 인스턴스 객체가 가지고 있는 변수
    ⭐ 인스턴스 객체가 생성될 때 생성 or 객체 생성 후 생성 가능
    
    ✅ self가 위치한 어디서나 선언 가능 but 
    보통 __ init__ 메서드(생성자) 안에서 선언
    
    ✔️ self
    인스턴스 객체를 가리키는 키워드
    
    self가 있는 곳에서 선언된 변수들은 인스턴스의 영역으로 간주되어 dot으로 호출
    
class Car:
    max_speed = 300
    def __init__(self, name): # self는 인스턴스 고유의 영역
        self.name = name
    def start(self, speed): # self는 인스턴스 고유의 영역
        self.speed = speed
        return f'{self.name}차가 {self.speed}의 속력으로 움직이고 있습니다.'

modelx = Car('Weniv Model X')
print(modelx.name) # Weniv Model X
print(modelx.start(100)) # Weniv Model X차가 100의 속력으로 움직이고 있습니다.

modely = Car('Weniv Model Y')
print(modely.name) # Weniv Model Y
print(modely.start(200)) # Weniv Model Y차가 200의 속력으로 움직이고 있습니다.

⚠️ 다른 인스턴스와 메모리 영역을 공유 ❌

class Car:
    speed = 300

def change_speed(self, speed):
    self.speed = speed

⚠️ self.speed는 상위에 있는 speed를 조작 ❌

 ✔️ 인스턴스와 클래스 변수의 변경
class Car:
    kinds = []
    def add_kinds(self, name):
        self.kinds.append(name) # == Car.kinds.append(name)
modelx = Car()
modely = Car()
modelx.add_kinds('modelx')
modely.add_kinds('modely')
print(modelx.kinds)
print(modely.kinds)

⚠️ self.kinds는 인스턴스 변수❌
➡️ self.kinds는 인스턴스 변수 / 
    but 예제에서 self.kinds.append로 참조만 하고 있음 -> 클래스 변수의 값 수정 ⭕
    
✅ 데코레이터를 사용하여 의도 표현 가능 (@classmethod: 클래스 변수를 수정함을 의미)
 
✔️ 인스턴스 변수 변경
    인스턴스 생성 후 dot를 통해 변수 추가 / 변경 가능
class Car:
    pass
modelx = Car()
modelx.speed = 500
modelx.color = 'red'
# Car class에는 speed, color 변수가 생성됨

print(modelx.speed) # 500
print(modelx.color) # red

✅ 함수도 동일 적용
def hello():
    print("hello world")
print(type(hello))  # <class 'function'>
hello.hi = "hi, world"
print(hello.hi)  # hi, world

⚠️ 내장되어 있는 자료형은 지원 ❌
```