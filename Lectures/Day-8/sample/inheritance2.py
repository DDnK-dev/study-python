class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def bark(self, sound):
		return f"{self.name}({self.age}): {sound}!"

class Yorkie(Dog):
	def bark(self, sound="...zzz"):
		return super().bark(sound)

koko = Yorkie("koko",5)
print(koko.bark())
