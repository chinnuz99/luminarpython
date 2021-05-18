#create employee class
class Employee:
    company="LT"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print("company name=",Employee.company)
        print("name of student",self.name)
        print("rolllno",self.age)
        print("salary",self.salary)
    def __str__(self):            #two strng method string is only possible
        #return self.name
        return self.name+str(self.age)+str(self.salary)
ob=Employee("anu",32,25000)
ob.printval()
print(ob)
#student name student rollno