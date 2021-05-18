#create person class using constructor,use inheritance in constructor
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)
class Student(Person):
    def __init__(self,rollno,mark,name,age,gender):
        super().__init__(name,age,gender)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
cr=Student(2,34,"anu",22,"female")
cr.printval()
cr.print()
