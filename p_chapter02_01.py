# Chapter02-01
# python 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심으로 코딩 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
car_company_1 = 'ferrari'
car_detail_1 = [
    {'color':'white'},
    {'horsepower':400},
    {'price':8000}
]

# 차량2
car_company_2 = 'bmw'
car_detail_2 = [
    {'color':'black'},
    {'horsepower':270},
    {'price':5000}
]

# 차량3
car_company_3 = 'audi'
car_detail_3 = [
    {'color':'silver'},
    {'horsepower':300},
    {'price':6000}
]


# List 구조 / 관리하기가 불편, Index 접근시 실수 가능성, 삭제 불편(Index 번호를 알아야함)
car_company_list = ['ferrari','bmw','audi']
car_detail_list = [
    {'color':'white','horsepower':400,'price':8000},
    {'color':'black','horsepower':270,'price':5000},
    {'color':'silver','horsepower':300,'price':6000},
]

del car_company_list[1]
del car_detail_list[1]

print([car_company_list])
print([car_detail_list])

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(Key), Key 조회 예외 처리 등

car_dicts = [
    {'car_company' : 'ferrari', 'car_detail': {'color' : 'white','horsepower' : 400, 'price' : 8000}},
    {'car_company' : 'bmw', 'car_detail': {'color' : 'black','horsepower' : 270, 'price' : 5000}},
    {'car_company' : 'audi', 'car_detail': {'color' : 'silver','horsepower' : 300, 'price' : 6000}}
]

print([car_dicts])

# pop(key,'default')
del car_dicts[1]
print([car_dicts])

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class car():
    def __init__(self, company,detail):
        self.company = company
        self.detail = detail

#원하는 방식으로 보여줌, 사용자를 위한 표현, str 이 없어야 repr로 표시됌
    def __str__(self):
        return 'str : {} - {}'.format(self.company, self.detail)
#객체를 그대로 표현
    def __repr__(self):
        return 'repr : {} - {}'.format(self.company, self.detail)

    def __reduce__(self):
        pass

car1 = car('ferrari',{'color' : 'white','horsepower' : 400, 'price' : 8000})
car2 = car('bmw',{'color' : 'white','horsepower' : 270, 'price' : 5000})
car3 = car('audi',{'color' : 'white','horsepower' : 300, 'price' : 6000})

print(car1)
print(car2)
print(car3)

#속성 정보를 알 수 있음
print(car1.__dict__)
print(dir(car1))

print()
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

for x in car_list:
    print(x)
