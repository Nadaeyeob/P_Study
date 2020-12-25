# Chapter04-01
# 시퀀스형
    # 컨테이너(Container : 서로 다른 자료형[List, tuple, collection.deque])
    # 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, memoryview])

# 가변형 (List, bytearray, array.array, memoryview, deque)
# 불변형 (tuple, str, bytes)

# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending List)
chars = '+_)(*&^%$#@!~)'
# chars[2] = 'h' -> 불변형으로 재할당 불가

code_list1 = []

for s in chars:
# 유니코드 리스트
    code_list1.append(ord(s))
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list4)


print([chr(s) for s in code_list1])

print()
print()

# Generator 생성 ( __iter__ 가 있으면 for 로 순회가 가능하다)
import array

# Generator : 한 번에 한개의 항목을 생성 (메모리 유지 x)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I',(ord(s) for s in chars))

print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist()) # -> I 는 어디로?

# Generator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)

print()
print()

# List 주의
mark1 = [['~'] * 5 for n in range(5)]
mark2 = [['~'] * 5] * 5
# = mark1 = [['~'] * 5 for _ in range(5)]
print(mark1)
print(mark2)

# 수정
mark1[0][1] = 'X'
mark2[0][1] = 'X'
print(mark1)
print(mark2)

# 증명
print([id(i) for i in mark1]) # -> 서로 4개가 다름
print([id(i) for i in mark2]) # -> 4개가 서로 같음
