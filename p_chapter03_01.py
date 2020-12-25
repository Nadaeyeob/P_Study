# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드 , Low level
# __ 로 시작하는 .. for example : __init__ , __repr__

# 기본형
print(int) # 생각하지 않고 썼던 Data Type은 Class 였다..
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10
print(type(n))

print(n + 100)
print(n.__add__(100)) # __add__
# print(n.__doc__)
print(n.__bool__(),bool(n))
print(n*100,n.__mul__(100))

print()
print()

# Class 예졔1
class fruit:
    def __init__(self,name,price):
        self._name = name
        self._price = price
    def __str__(self):
        return 'fruit class info : {} , {}'.format(self._name,self._price)

    def __add__(self, x):
        print('called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('called __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('called __le__')
        if self._price <= x._price:
            return True
        else:
            return False
    def __ge__(self, x):
        print('called __ge__')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = fruit('orange',7500)
s2 = fruit('banana',3000)

# Magic Method 사용 하지 않을 경우
print(s1._price + s2._price)
# Magic Method 사용 했을 경우
print(s1+s2)
print(s1-s2)
print(s1>=s2)
print(s1<=s2)
