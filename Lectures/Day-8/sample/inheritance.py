class Parent:
    hair_color = "brown"
    def __init__(self):
        self.language = ["English"]
    def says(self):
        print(f"She said in {self.language[-1]}, 공부해라")

class Child(Parent):
    hair_color = "black"
    def __init__(self):
        super().__init__()
        self.language.append("Korean")
    def says(self):
        print(f"He answered in {self.language[-1]}, 싫어요!")

ally = Parent()
joe = Child()
print(joe.hair_color) # black
print(joe.language) # ['English', 'Korean']

print(ally.language)
print(ally.hair_color)

ally.says()
joe.says()