# Chapter04-02
# 시퀀스형
    # 컨테이너(Container : 서로 다른 자료형[List, tuple, collection.deque])
    # 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, memoryview])

# 가변형 (List, bytearray, array.array, memoryview, deque)
# 불변형 (tuple, str, bytes)

# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b (다른 언어의 경우 임시 변수 사용하여 해야함)

print(divmod(100,9))
print(divmod(*(100,9))) # -> *이 없으면 (100,9)를 한개로 인식하여 Error
print(*(divmod(100,9))) # -> * (11,1) 를 11 1 로 한개로 만들어버림

print()
print()

x, y, *rest = range(10)
print(x,y, rest)
x, y, *rest = range(2)
print(x,y,rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x,y,rest)

print()
print()

# Mutable(가변) vs Imutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l *2
m = m *2

print(l, id(l))
print(m, id(m))

l *=2
m *=2

print(l, id(l)) # Tuple은 계속 바뀜, (고유값이 불변이라 동일 id 사용 불가)
print(m, id(m))

print()
print()

# sort vs sorted
# revers, key = len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange','apple','banana','mango','papaya','lemon','strawberry','coconut']


print(f_list)
print(sorted(f_list))
print(sorted(f_list, reverse=True))
print(sorted(f_list, key=len))
print(sorted(f_list, key=lambda x: x[-1])) # 끝 글자 기준으로 정렬
print(sorted(f_list, key=lambda x: x[-1], reverse=True))
print(f_list) # 종료후 맨 처음 Data와 동일

# sort : 정렬 후 객체 직접 변경 (원본을 그대로 사용)

print(f_list)
print(f_list.sort(),f_list)
print(f_list.sort(reverse=True),f_list)
print(f_list.sort(key=len),f_list)
print(f_list.sort(key=lambda x : x[-1]),f_list)
print(f_list.sort(key=lambda x : x[-1],reverse=True),f_list)

# List vs Array 적합한 사용법 설명
# List 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(List와 거의 호환)
