class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee:
    def print(self,company):
        self.company=company
        print(self.company)
class Child(Person,Employee):
    def info(self,place,id):
        self.place=place
        self.id=id
        print(self.place)
        print(self.id)
per=Person()
per.details("anu",25,"female")
em=Employee()
em.print("abc")
ch=Child()
ch.details("amal",27,"male")
ch.print("xyz")
ch.info("ernklm",120)
