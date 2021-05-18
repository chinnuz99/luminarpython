class Student:
    School="abc"
    def __init__(self,name,age,rollno,mark):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.mark=mark
    def printdetails(self):
        print("college name",Student.School)
        print("name of student",self.name)
        print("age of student",self.age)
        print("roll no of student",self.rollno)
        print("mark",self.mark)
    def __str__(self):
        return self.name + str(self.rollno)

obj=Student("anu",18,22,80)
obj.printdetails()
print(obj)

