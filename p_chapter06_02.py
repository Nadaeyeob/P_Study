# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러일을 쉽게 해결
# 병행성의 경우 언제 멈추고 진행했는지를 기억해야함

# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1

def generator_ex1():
    print('start')
    yield 'A Point' # yield 기준에서 멈춰있음
    print('Continue')
    yield 'B point'
    print('End')

temp = iter(generator_ex1())

#print(temp)
print(next(temp)) # iter로 되있기 때문에 next 사용 가능, A point에 멈춰있음
print(next(temp)) # B point
# print(next(temp)) -> error 발생

print('*' * 20)
for v in generator_ex1():
    print(v) # -> for 구문은 예외처리까지 해주므로 error 미발생

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()] # -> Yield keyword 뒤에 있는 구문 3번 반복
temp3 = (x * 3 for x in generator_ex1()) # -> 그냥 Generaor 로 반복문으로 표시

print(temp2,temp3)

for i in temp3:
    print(i)

for i in temp2:
    print(i)


print()
print()

# Generator Ex3 (중요 함수)
# count, takewhile, filter false, accumulate, chain, product, groupby...

import itertools

gen1 = itertools.count(1,2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))

# while True:
#     print(next(gen1)) 실제 실행시 계속 증가하여 실행 불가능

# 조건

gen2 = itertools.takewhile(lambda n : n < 50, itertools.count(1,2.5))

for v in gen2:
    print(v)

print()
print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,10)])

for v in gen4:
    print(v)

# 연결1
gen5 = itertools.chain('ABCDE',range(1,11,2))
print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE')) #tuple 용 list로 출력
print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print('\n' , list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=4)
print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))
