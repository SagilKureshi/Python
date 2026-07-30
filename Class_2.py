class Student:
    def __init__(self):
        self.name = "abc"
        self.age = 30
        self.marks = 89

    def talk(self):
        print("Name = ",self.name)
        print("age = ",self.age)
        print("marks = ",self.marks)

p1 = Student()
p1.talk()
