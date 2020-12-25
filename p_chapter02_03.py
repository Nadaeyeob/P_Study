# Chapter02-03

class car():
    """
    car class
    author : kim
    date:2020:09.27
    Description : Class, Static, Instance Method
    """

#Class 변수 선언 지역
#Class 변수 (모든 Instance가 공유)
    price_per_raise = 1.0

# self : instace,  method : self가 변수로 받음

    def __init__(self, company,detail):
        self._company = company
        self._detail = detail

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._detail)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._detail)

    # Instance method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('current ID : {}'.format(id(self)))
        print('car detail info : {0} {1}'.format(self._company,self._detail.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company,self._detail.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company,self._detail.get('price')*car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! Price increased.')

    # Static Method (Inst는 임의로 설정한 값...)
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'bmw':
            return 'OK! this car is {}'.format(inst._company)
        return 'Sorry, this car is not BMW'



# self의 의미 -> 고유의 값을 지정하기 위한 지시어
car1 = car('ferrari',{'color' : 'white','horsepower' : 400, 'price' : 8000})
car2 = car('bmw',{'color' : 'white','horsepower' : 270, 'price' : 5000})

# 전체정보
car1.detail_info()

# 가격정보(직접 접근)
print(car1._detail.get('price'))
print(car1._detail['price'])

# 가격정보(인상 전 Method 사용)
print(car1.get_price())
print(car2.get_price())

# 가격정보(인상 전 class Method 미사용)
car.price_per_raise = 1.4

print(car1.get_price_culc())
print(car2.get_price_culc())


# Class Method
car.raise_price(1.6)
print(car1.get_price_culc())
print(car2.get_price_culc())

# Static Method
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(car.is_bmw(car1))
