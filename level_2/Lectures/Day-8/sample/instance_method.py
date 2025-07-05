class Employee:
    company = "my-company"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print("집에 보내주세요")
    def speak(self, sound):
        return f"{self.name} says, {sound}"

ken = Employee("ken", 23)
ken.work()  # 집에 보내주세요
print(ken.speak("나는 일이 좋아"))
