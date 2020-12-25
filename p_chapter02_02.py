# Chapter02-02

class car():
    """
    car class
    author : kim
    date:2020:09.27
    """

#Class 변수 선언 지역
    car_count = 0

# self : instace,  method : self가 변수로 받음
    def __init__(self, company,detail):
        self._company = company
        self._detail = detail
        car.car_count +=1
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._detail)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._detail)

    def __del__(self):
        print('del method')
        car.car_count -=1

    def detail_info(self):
        print('current ID : {}'.format(id(self)))
        print('car detail info : {0} {1}'.format(self._company,self._detail.get('price')))

# self의 의미 -> 고유의 값을 지정하기 위한 지시어
car1 = car('ferrari',{'color' : 'white','horsepower' : 400, 'price' : 8000})
car2 = car('bmw',{'color' : 'white','horsepower' : 270, 'price' : 5000})
car3 = car('audi',{'color' : 'white','horsepower' : 300, 'price' : 6000})

# ID 확인 -> self는 각각을 의미함, id가 모두 다르기 때문..
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # Value를 비교
print(car1 is car2) # ID를 비교 (instance)

# dir & __dict__
print(dir(car1)) #dir 해당 instance가 가지고 있는 attribute를 다 보여줌
print(dir(car2)) #상속 받는 모든 걸 보여줌

print()
print()

print(car1.__dict__) # __dict__ 선언한 것만 자세히 보여줌
print(car2.__dict__)

# Doctring
print("---Doctoring---")
print(car.__doc__)

# 실행
car1.detail_info()

print()
print()

# 비교
print("--- Instance comparing by id ---")
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__)) # Instance 값은 상이하지만, Class 가 같아서 ID가 같음

# 에러
car2.detail_info() # -> self를 자동으로 input
car.detail_info(car2) # -> self를 ()안에 명기

print()
print()

# Class 변수 공유확인
print(car1.car_count)
print(car1.__dict__) # Class 변수 확인 불가
print(dir(car1)) # Class 변수 확인 가능 -> Class 변수가 아닌 경우 _ 를 안붙여서 구분하는게 약속

# 접근
print(car1.car_count)
print()
print(car.car_count)

del car2
#삭제 확인
print(car1.car_count) # Car1 에는 car_count가 없지만, 상위로 찾아 class car를 찾아 class 변수를 찾으러 감
print(car.car_count)

# instance namespace에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위 검색함 (클래스 변수, 부모 클래스 변수))
