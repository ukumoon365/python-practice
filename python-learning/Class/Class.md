# Class
```text
✔️ Class
    공통의 데이터, 기능을 묶어 관리

✔️ 인스턴스
    클래스를 통해 만들어진 것
    같은 클래스로 만들면 내용은 같지만 서로 다른 객체 A is B # False


✔️ 클래스 분석
ex) 
    l = [1, 2, 3]
    print(type(l))
    print(dir(l))
    
    # 
    <class 'list'>
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


class Car:
    max_speed = 300
    max_people = 5 
    def start(self): # 메서드
        print('차가 출발합니다!')
    def stop(self): # 메서드
        print('차가 멈췄습니다!')
modelx = Car()
print(type(modelx))
print(dir(modelx))       

#
<class '__main__.Car'>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'max_people', 'max_speed', 'start', 'stop']

⭐ 클래스를 정의하면 기본적으로 object 클래스로부터 상속받는 기능 제공 
⭐ 파이썬의 클래스는 기본적으로 object 클래스를 상속 
(dir()을 사용하면 상속받은 기능과 해당 클래스에서 직접 정의한 속성 및 메서드를 확인 가능)

✔️ 장점
    - 속도 향상
    - 재사용성
    - 유지보수
```