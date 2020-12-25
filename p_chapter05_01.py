# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 (return)

# 함수 객체

def factorial(n):
    '''
    factorial function -> n : int
    '''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial),type(A))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial # var_func = factorial(10) 과 다름
print(var_func)
print(var_func(10))
print(map(var_func, range(1,11)))
print(list(map(var_func, range(1,11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
print(list(map(var_func,filter(lambda x: x % 2, range(1,6))))) #익명함수 lambda
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1,11))) # -> range (1,11) = [1,2,3, ... ,10] reduce는 하나씩 줄이면서 계산 1+2 이후 1,2 삭제 ..
print(sum(range(1,11)))

# 익명함수(Lamda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x+t, range(1,11))) # add = lamda x, t: x+t

print()
print()

# callable : 호출 연산잔 -> 메소드 형태로 호출 가능
# 호출 가능 확인

print(callable(str), callable(A), callable(list), callable(var_func), callable(factorial), callable(3.14)) # -> 3.13(3) 이런게 안되니..

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul # 위에서 from operator import add, mul 로도 가능
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5) # -> 일급 객체로 함수를 인수로 전달, 함수를 변수에 전달 (5*?)
print(five(10))
# 고정 추가
six = partial(five,6)
print(six()) # print(six(10)) 등으로 넣으면 Error 발생, mul은 두개 인수만 받음
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))
