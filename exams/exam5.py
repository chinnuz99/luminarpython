#What is method overriding give an example using Books class?
#over riding means same method name and same signatures.
#eg:
class Book:
    def details(self,model):
        self.model=model
        print ("the book model is",self,model)
class Author(Book):
    def details(self,mode):
        self.mode=mode
        print("the book has to be",mode)
st=Author()
st.details(1)


