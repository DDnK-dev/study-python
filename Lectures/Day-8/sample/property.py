class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # aget -> _age

    @property
    def age(self):
        print("나이를 리턴합니다.")
        return self._age

    @age.setter
    def age(self, age_value):
        if age_value < 0:
            print("나이는 0보다 작을 수 없습니다.")
            return
        if age_value < self._age:
            print("나이는 줄어들 수 없습니다.")
            return
        self._age = age_value

jongho = Person("jongho", 23)
print(jongho.age)
jongho.age = 10
print(jongho.age)
# 23
# 10
print(jongho.__dict__)