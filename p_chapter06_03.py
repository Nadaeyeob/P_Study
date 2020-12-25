# Chapter06-03
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러일을 쉽게 해결
# 병행성의 경우 언제 멈추고 진행했는지를 기억해야함
# 코루틴(Coroutine)

# Coroutine : 단일(Single) 쓰레드, 스택을 기반으로 동작하는 비동기 작업
# thred : os 관리, CPU core에서 실시간, 시분할 비동기 작업 -> Multi thred
# yield : 메인 <-> 서브

# Subroutine : Main routine 호출 -> Subroutine에서 수행(흐름제어)
# Coroutine : routine 실행 중 중지 -> 동시성 프로그래밍, thred에 비해 overhead 감소
# thred : Single thred -> multi thred -> 복잡 (공유되는 자원, Dead Lock - 교착 상태 발생 가능성), 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# python 3.5 이상에서 def -> async, yield -> await

# Coroutine ex1

def coroutine1():
    print('>>> coroutine started')
    i = yield # yield -> Generater
    print('>>> coroutine received : {}'.format(i))

# Main routine
# Generater 선언

cr1= coroutine1()

print(cr1,type(cr1)) # Generater 확인 가능
# yield 지점까지 Subroutine 수행
next(cr1)
# next(cr1) -> 예외 발생으로 Error, 기본값으로 None 전달

# 값 전송
# cr1.send(100) -> i에 100을 받음

# 잘못된 사용
cr2 = coroutine1()
# cr2.send(100) -> Error 발생, yield 까지 가지 못해서 실행 불가, Next로 시작 필요

# Coroutine ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x): # 값(인자)을 줌으로써 sub routine에 준다고 생각하면 되나..
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x+y
    print('>>> coroutine received : {}'.format(z))
    a = yield z
    print('>>> coroutine received : {}'.format(a))


print('---')
from inspect import getgeneratorstate

cr3 = coroutine2(10)
print(getgeneratorstate(cr3))
print(next(cr3))
print(getgeneratorstate(cr3))
cr3.send(100) # send에서 값이 넘어오는걸 보려면 print()로 출력, ex) z:  main routine -> sub routine / x+y : sub routine -> main routine
print(getgeneratorstate(cr3))

print()
print('---')

# Coroutine ex3
# stopiteration 자동 처리 (3.5 이상에서 await 사용시 처리됌)
# 중첩 Coroutine

def generator1():
    for x in 'AB':
        yield x

    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1)) # 맨 처음 for 구문 끝나고 시작
print(next(t1))

t2 = generator1()
print(list(t2)) # ->알아서 next 호출 및 List 반환

print('---')
def generator2():
    yield from 'AB' # for 구문 대신 yield from으로 대체
    yield from range(1,4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))

print('---')
