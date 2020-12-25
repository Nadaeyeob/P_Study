# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의할ㄷ 수 있는 특별한(Built-in) 메소드 , Low level
# __ 로 시작하는 .. for example : __init__ , __repr__


# Class 예졔2
# 벡터(x,y)
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# max((5,10)) = 10

class vector(object):
    def __init__(self,*args): # packing -> (x,y) 로 선언하지 않고, (x,y)를 args 로 packing 함
        '''
        create a vector, example : v = vector(5,2)
        '''
        if len(args) == 0: # 예외처리
            self._x, self._y = 0,0 # unpacking

        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        return the vector information.
        '''
        return 'vector(%r,%r)' %(self._x,self._y)

    def __add__(self, other):
        '''
        return the vector add self and otehr
        '''
        return vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        '''
        return the vector multiply self and otehr
        '''
        return vector(self._x * other, self._y *other)

    def __bool__(self):
        return bool(max(self._x,self._y))

print(vector.__init__.__doc__)

#vector 인스턴스 생성
v1 = vector(5,7)
v2 = vector(23,35)
v3 = vector()

# Magic Method 생성 -> magic method를 class 안에 넣어서 함수로 표현하게끔 함

print(v1+v2)
print(v1*5)
