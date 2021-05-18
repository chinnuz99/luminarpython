#person,child,parent,student
#child,parent_    person
#student class_     child
class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Child(Person):
    def print(self,empid,post):
        self.empid=empid
        self.post=post
        print(self.empid)
        print(self.post)
class Parent(Person):
    def info(self,salary,experience):
        self.salary=salary
        self.experience=experience
        print(self.salary)
        print(self.experience)
class Student(Child):
    def det(self,std,sub):
        self.std=std
        self.sub=sub
        print(self.std)
        print(self.sub)
per=Person()
per.details("anu",24,"female")
ch=Child()
ch.details("achu",24,"male")
ch.print(1,"SM")
p=Parent()
p.details("appu",23,"male")
p.info(50000,4)
st=Student()
st.details("anju",26,"female")
st.print(2,"HR")
st.det(10,"python")




