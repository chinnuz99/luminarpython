class Student:
    def __init__(self,name,age,rollno,college):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.college=college
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.rollno)
        print(self.college)
stu=Student("pooja",20,12,"luminar")
stu.printval()
