##employee attributes name,age,id,salary,deparment,company
class Employee:
    def details(self,name,age,id,email,salary,department,company):
        self.name=name
        self.age=age
        self.id=id
        self.email=email
        self.salary=salary
        self.department=department
        self.company=company
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.email)
        print(self.salary)
        print(self.department)
        print(self.company)
obj=Employee()
obj.details("anoop",29,1608,"anoop12@gmail.com",25000,"assistant manager","mrf")
obj.printval()