#Create an Animal class using constructor and build a child class for Dog?
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print("i'am",self.name)
        print(self.age,"years old")
class Dog(Animal):
    def __init__(self,name,age,type):
        super().__init__(name,age)
        self.type=type
    def printval(self):
        print(self.type)
am=Dog("jacky",5,"dog")
am.print()
am.printval()




