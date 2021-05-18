#Create an example for three types of inheritance in one program by using Person as main class
class Person:
    def print(self,name,age):
        self.name=name
        print(self.name)
class Student:
    def printval(self,age):
        self.age=age
        print(self.age)
class print(Person):
    def m(self):
        print("details:")
class Parent(Person,Student):
    def det(self,job):
        self.job=job
        print(self.job)
class Employee(Parent)
    def details(self,salary):
        self.salary=salary
        print(self.salary)
per=Person()
per.print("anu")
st=Student()
st






