from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # 추상 메서드는 구현하지 않음

class Dog(Animal):
    def make_sound(self):
        return "멍멍!"

class Cat(Animal):
    def make_sound(self):
        return "야옹!"

class Rat(Animal):
    # make_sound를 구현하지 않은것에 주의해주세요
    def some_sound(self):
        return "찍찍!"

dog= Dog()
cat= Cat()
rat= Rat()
