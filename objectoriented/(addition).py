#addition program using class (object oriented)
# class Addition:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#     def printval(self):
#         print(self.a+self.b)
# obj=Addition()
# obj.add(10,10)
# obj.printval()

class Add:
    def setval(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print("res",self.num1+self.num2)
obj=Add()
obj.setval(20,10)
obj.printval()
