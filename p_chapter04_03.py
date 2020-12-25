# Chapter04-03
# 시퀀스형
    # 컨테이너(Container : 서로 다른 자료형[List, tuple, collection.deque])
    # 플랫(Flat : 한개의 자료형 [str, bytes, bytearray, array.array, memoryview])

# 가변형 (List, bytearray, array.array, memoryview, deque)
# 불변형 (tuple, str, bytes)

# 해시테이블
# Key에 Value를 저장하는 구조
# 파이썬 dict -> 해쉬 테이블의 예
# Key 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수 -> 해쉬 주소 -> Key에 대한 Value 참조 (위치 파악)

# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30,40,50)) # ->Tuple
t2 = (10, 20, [30,40,50]) # ->Hash

print(hash(t1))
# print(hash(t2)) -> List는 Mutable 값으로 Hash 값 없음 (오류발생)

print()
print()

# Dict setdefault 예제
source = (('k1','val1'),
         ('k1','val2'),
         ('k2','val3'),
         ('k2','val4'),
         ('k2','val5')) # tuple로 된 data를 dict로 전환

new_dict1 ={}
new_dict2 ={}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k,v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3={k: v for k,v in source}
print(new_dict3)
