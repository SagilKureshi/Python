class Demo:
    def __init__(self):
        self.x = 10 #Instance Variable

    def modify(self):
        self.x+=1

s1 = Demo()
s2 = Demo()
print("x using s1 :",s1.x)
print("x using s2 :",s2.x)
s1.modify()
print("x using s1 :",s1.x)
print("x using s2 :",s2.x)