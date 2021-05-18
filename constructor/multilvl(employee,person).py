class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def print(self,company,salary):
        self.company=company
        self.salary=salary
        print(self.company)
        print(self.salary)
class Staff(Employee):
    def info(self,post,experience):
        self.post=post
        self.experience=experience
        print(self.post)
        print(self.experience)
per=Person()
per.details("anu",23,"female")
em=Employee()
em.details("amal",24,"male")
em.print("TATA",25000)
sta=Staff()
sta.details("sona",25,"female")
sta.print("VIPRO",45000)
sta.info("HR",4)







