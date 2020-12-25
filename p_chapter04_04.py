# Chapter04-04
# 시퀀스형
# hashtable -> 적은 리소르로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X , Set -> 중복 허용 X (union 구글링)
# Dict 및 Set 심화

# immutable Dict

from types import MappingProxyType

d = {'key1':'value1'}

# read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen,id(d_frozen)) # -> 표면상으로 Read only가 됐을뿐 hash 값은 지원 # XXX:


# 수정 가능
d['key2'] = 'value2'
print(d)

# 수정 불가
# d_fozen['key2'] = 'value2'

print()
print()

s1 = {'apple', 'orange', 'apple', 'kiwi','apple'}
s2 = set(['apple', 'orange', 'apple', 'kiwi','apple'])
s3 = {3}
s4 = set() # 그냥 {}만 쓸경우 dict로 선언됌
s5 = frozenset({'apple', 'orange', 'apple', 'kiwi','apple'})

s1.add('melon')

print(s1)

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

print()
print()

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print('---')
print(dis('{10}'))
print('---')
print(dis('set([10])')) # 과정이 더 많음

# 지능형 집합 (comprehending set)

print('---')

from unicodedata import name
print({name(chr(i),'') for i in range(0,256)})
