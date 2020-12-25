# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입 (Iterable)
# collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 반복 가능한 이유 -> iter(x) 함수 호출
t = 'ABCDE'

print(dir(t)) # -> __iter__가 있음 (반복가능)

for c in t: # 내부적으로 Iter 호출, next 함수로 꺼냄
    print(c)

# while
w =iter(t)

print(dir(w)) # -> __next__
print(next(w))
print(next(w)) # A,B,C 순서로 나옴 -> 위치정보를 기억하고 있다.

print('---')
while True:
    try:
        print(next(w))
    except StopIteration:
        break
print() #-> next 다음 위치정보를 가지고있어서, C,D,E만 호출

# 반복형 확인
print(dir(t))
print(hasattr(t,'__iter__')) # -> True, 있다. dir()로 확인할 필요는 없음

from collections import abc
print(isinstance(t,abc.Iterable)) # Iterable Class를 상속받았는지 확인하는 방법

print()
print()

# next, Class 지만 Iterable 하게 만들었음
class wordsplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration. ^_^')
        self._idx +=1
        return word

    def __repr__(self): # overriding 다시 공부해야함
        return 'wordsplitter(%s)' % (self._text)

wi = wordsplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi)) 예외발생

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

class wordsplittergenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터, yield -> 위치정보 기억

        return # Return 없어도 됌

    def __repr__(self):
        return 'wordsplitter(%s)' % (self._text)

wg = wordsplittergenerator('Do today what you could do tomorrow')
wt = iter(wg)

print(wg)
print(wt) # Generator

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt)) 예외 발생
