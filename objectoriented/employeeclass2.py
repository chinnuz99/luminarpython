class Employee:
    company="mrf"
    def details(self,name,id):
        self.name=name
        self.id=id
    def printval(self):
        print("name",self.name)
        print("id",self.id)
        print("company",Employee.company)
obj=Employee()
obj.details("anoop",1608)
obj.printval()

obj2=Employee()
obj2.details("anoop",1608)
obj2.printval()