class Person:
    def __init__(self,name,city):
        self.name = name
        self.city = city

    def display(self):
        print("Name = ",self.name)
        print("City = ",self.city)

p1 = Person("name1","city1")
p2 = Person("name2","city2")

p1.display()
p2.display()
