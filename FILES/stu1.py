class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark = mark
    def printval(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("course:", self.course)
        print("mark:",self.mark)
    def __str__(self):
        return self.name
f=open("stu.txt","r")
for line in f:
    data = line.rstrip("\n").split(",")
    # print(data)
    name = data[0]
    rollno= data[1]
    course=data[2]
    mark=data[3]
    obj = Student(name,rollno,course,mark)
    print(obj)
    obj.printval()

#190 above mark student details
