#create employee class and use inheritance in it
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)
class Employee(Person):
    def __init__(self,company,salary,name,age,gender):
        super().__init__(name,age,gender)
        self.company=company
        self.salary=salary
    def print(self):
        print(self.company)
        print(self.salary)
st=Employee("LUMINAR",25000,"anu",25,"female")
st.printval()
st.print()