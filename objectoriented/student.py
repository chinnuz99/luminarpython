#type of variables
#instance variable, related to methods     #call self
#class variable ,classs variable related to class       #call class name
class Student():
    college="luminar"              #class variables related to class
    def setval(self,name,id):
        self.name=name
        self.id=id
    def printval(self):
        print("name",self.name)
        print("id",self.id)
        print("college",Student.college)
st=Student()
st.setval("parvathy",6)
st.printval()

st2=Student()
st2.setval("parvathy",6)
st2.printval()