class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def is_enlisted_in_military(self):
		return (self.age > 20)

jongho = Person("jongho", 23)
# ....
jongho.age = 10
# ...
print(jongho.is_enlisted_in_military()) # False, 의도한 결과가 아님
