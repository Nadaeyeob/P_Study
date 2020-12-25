# Chapter05-02
# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# ex1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10) -> b가 없기 때문에 error 발생

# ex2
b=20 # -> gloabl 변수

def func_v2(a):
    print(a) # -> local 함수
    print(b)

func_v2(10)

# ex3
c = 30

def func_v3(a):
    print(a)
    print(c)
    c = 40

# func_v3(10) -> error 발생

# def func_v3(a):
#     c = 40
#     print(a)
#     print(c)

# func_v3(10) -> error 미발생

def func_v3(a):
    c = 40
    print(a)
    print(c)

print('>>',c) # -> gloabl 변수로 30 반환
func_v3(10)
print('>>>',c) # -> 함수 실행 후 변수 변경 없음

d=30

def func_v4(a):
    global d
    print(a)
    print(d)
    d= 40

print('>>',d) # -> 함수 실행전으로 30 반환
func_v4(10)
print('>>>',d) # -> 함수 실행후로 40 반환

# closure(클로저) 사용 이유 (불변 상태를 기억한다라는 개념으로 알고있자)
# 서버 프로그래밍 -> 동시성(concurrency)제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 방법 ->Erlang
# 클로저는 공유하되 변경되지 않는(immutable, read only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom(일관성),STM - 멀티스레드(Coroutine) 프로그래밍에 강점

print()
print()

a = 100
print(a + 100)
print(a + 1000) # -> 1200을 나오게 하려면 (결과값 누적) 상태를 기억해야함

# 결과 누적 (함수 사용)
print(sum(range(1,51)))

# class 이용
class averager():
    def __init__(self):
        self._series =[]

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = averager()

# 누적 (상태를 기억했다가 load 해서 가져온다..)
print(averager_cls(10)) # -> 클래스 인스턴스를 함수처럼 실행 중 (__call__)
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(193))
