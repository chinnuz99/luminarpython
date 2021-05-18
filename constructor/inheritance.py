#method and attributes are puted on sub classes
#single inheritance
class Person:                                   #spr class/base class/parent class
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):                          #derived class/sub class/child class
    def print(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)

per=Person()
per.setval("anu",23,"female")
st=Student()
st.print("cs","abc")
st.setval("amal",25,"male")



#calculator attributes two numbers
#methods add,sub,divi,mul
