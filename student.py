from teacher import Teacher
class Student(Teacher):
    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

s = Student()
s.setId(64)
s.setName("name2")
s.setAddress("Asia")
s.setMarks(86)

print("id : ",s.getId())
print("name : ",s.getName())
print("address :",s.getAddress())
print("Marks : ",s.getMarks())