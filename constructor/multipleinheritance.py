class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Mobile:
    def print(self):
        print("i have 1+")
class Child(Person,Mobile):
    def info(self,college,place):
        self.college=college
        self.place=place
        print(self.college)
        print(self.place)
per=Person()
per.details("anu",25)
mob=Mobile()
mob.print()
ch=Child()
ch.details("amal",24)
ch.print()
ch.info("abc","ernklm")
