class Father:
    def height(self):
        print("6.0 foot")

class Mother:
    def color(self):
        print("White")

class Child(Father,Mother):
    pass

c_obj = Child()
c_obj.height()
c_obj.color()

