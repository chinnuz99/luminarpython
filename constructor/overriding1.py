class Parent:
    def details(self):
        print("my name is:varun")
    def print(self):
        print("company is: luminar")
class Child(Parent):
    def print(self):
        print("location is: kakkanad")
obj=Child()
obj.print()