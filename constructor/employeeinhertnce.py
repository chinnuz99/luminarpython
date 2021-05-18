class Person:
    def details(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
        print(self.name)
        print(self.age)
        print(self.id)
class Employee(Person):
    def print(self,department,company):
        self.department=department
        self.company=company
        print(self.department)
        print(self.company)
per=Person()
per.details("pooja",23,153)
em=Employee()
em.print("supervioser","tata")
em.details("arun",25,160)