class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printdata(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
lst=[]
f=open("exam6.txt","r")
for i in f:
    data =i.rstrip("\n").split(",")
    #print(data)
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=data[3]
    s1=Student(name,rollno,course,mark)
    lst.append(s1)
mark=[]
for st in lst:
    mark.append(st.mark)
print(mark)
for st in lst:
    if(st.mark==max(mark)):
       print(st.rollno,st.name,st.mark)
