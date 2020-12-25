# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(reference) 복사 후 저장 -> 후에 접근(엑세스) 가능

# closure 사용
def closure_ex1():
    # Free variable
    # closure 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series,len(series)))
        return sum(series) / len(series)
    return averager # 함수 결과 변화 가능(return) _ 일급 함수

avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars) # series를 가지고 있음
print(avg_closure1.__closure__[0].cell_contents) # 0 대신 1을 넣으면 안됌, Tuple 형식이라는데 왜?

print()
print()

# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) -> error 발생, 예외 발생

def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(30))
print(avg_closure3(50))
