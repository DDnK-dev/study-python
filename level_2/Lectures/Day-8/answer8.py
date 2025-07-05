# 1.3

"""
2번
class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print(f"{self.name}! 걷는다!")
    def __str__(self):
        print(f'{self.name}의 나이는 {self.age}살이다.')

class Dog(animal):
    def bark(self):
        print(f'{self.name}: 멍멍!')

class Bird(animal):
    def fly(self):
        print(f'{self.name}: 훨훨!')

class Cat(animal):
    def climb(self):
        print(f'{self.name}: 나무를 탄다!')

dog = Dog("멍멍이", 3)
bird = Bird("구구", 2)
cat = Cat("야옹이", 4)
"""

""" 3번
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str = None
    age: int = None
    def __post_init__(self):
        print(f'{self.name}님의 나이가 {self.age}살이군요')
    def __str__(self):
        print(f'이름:{self.name} 나이:{self.age}')
"""

from dataclasses import dataclass, field

@dataclass
class Person:
    _name: str = None
    _age: int = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name_value):
        if type(name_value) == str:
            self._name = name_value
        else:
            print("잘못된 입력입니다")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age_value):
        if type(age_value) == int:
            self._age = age_value
        else:
            print("잘못된 입력입니다")

    def __post_init__(self):
        print(f'{self._name}님의 나이가 {self._age}살이군요')
    def __str__(self):
        print(f'이름:{self._name} 나이:{self._age}')

uuii = Person(31,"종민")
