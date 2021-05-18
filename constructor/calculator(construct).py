class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("number1=",self.a)
        print("number2=",self.b)
    def add(self):
        print("add=",self.a + self.b)
    def sub(self):
        print("sub=",self.a - self.b)
    def mul(self):
        print("mul=",self.a * self.b)
    def div(self):
        print("div=",self.a / self.b)
cl=Calculator(6,3)
cl.add()
cl.sub()
cl.mul()
cl.div()