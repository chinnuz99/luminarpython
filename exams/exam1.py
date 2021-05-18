#Create a child class Bus that will inherit all of the variables and methods of Vehicle class?
class Vehicle:
    def __init__(self,number,place):
        self.number=number
        self.place=place
    def printval(self):
        print("num",self.number)
        print("place",self.place)
class Bus(Vehicle):
    def __init__(self,number,place,name):
        super().__init__(number,place)
        self.name=name
    def print(self):
        print("name",self.name)
bs=Bus(1234,"ksd","hanna")
bs.printval()
bs.print()

