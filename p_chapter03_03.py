# Chapter03-03
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의할ㄷ 수 있는 특별한(Built-in) 메소드 , Low level
# __ 로 시작하는 .. for example : __init__ , __repr__

# 객체 -> 파이썬의 데이터를 추상화 한다 : 객체 지향, Overiding (overiding이 무엇일까..)
# 모든 객체 -> id, type -> Value

# 일반적인 튜플
point1 = (1.0,5,0)
point2 = (2.5,1.5)

from math import sqrt

l_leng1 = sqrt((point1[0] - point2[0]) **2 + (point1[1] - point2[1]) **2)
print(l_leng1)

# namedtuple, what is namedtuple in python in google
from collections import namedtuple

#namedtuple 선언
point = namedtuple('point','x y') # Space 바로 x y 구분

point3 = point(1.0,5.0)
point4 = point(2.5,1.5)

print(point3)
print(point3[0]) # Tuple
print(point3.x) # Dic
print(point4)

l_leng2 = sqrt((point3.x - point4.x) **2 + (point3.y - point4.y) **2)
print(l_leng2)

#namedtuple 선언 방법
point5 = namedtuple('point',['x','y'])
point6 = namedtuple('point','x, y')
point7 = namedtuple('point','x y')
point8 = namedtuple('point','x y x class',rename=True) # 예약어나 (class), 중복값은 쓸 수 없음 -> rename = True가 필요, Default = False

# 출력
print(point5,point6,point7,point8)

# Dic to Unpacking
temp_dict = {'x' : 75, 'y' : 55}
p9 = point5(**temp_dict) # Tuple은 * , Dict는 **로 Unpacking


p5 = point5(x=10,y=35)
p6 = point6(20,40)
p7 = point7(45,y=20)
p8 = point8(10,20,30,40)

print("--- print example ---")
print()
print(p8) #중복되었던 x를 _2로, 예약어(class)는 _3으로 알아서 바꿈
print(p9)

print(p5.x + p6.y)
# Unpacking
x,y = p5
print(x,y)

# Namedtuple Method

# _make() : 새로운 객체 생성, List를 Naemdtuple로 전환
temp = [52,38]
p1 = point5._make(temp)
print(p1)

# _fields : 필드 네임 확인
print(p1._fields,p5._fields)

# _asdict() : ordereddict 반환
print(p5._asdict())

# 실 사용 실습
# 반 20명, 4개 반(A,B,C,D) -> A08, B14

classes = namedtuple('classes', ['rank','number'])

# Group List 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split() # 공백을 기준으로 List 화 = ['A','B','C','D']

# List Comprehension
student = [classes(rank, number) for rank in ranks for number in numbers]

print(len(student))
print(student)

# 추천 : 변수 호울 X
student2 = [classes(rank, number)
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)]]

print(len(student2))

# 출력
for s in student:
    print(s)
