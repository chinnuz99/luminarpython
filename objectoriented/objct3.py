#same classinte underil varunna attributes
class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
obj=Person()
obj.details("parvathy",22)
obj.printval()
