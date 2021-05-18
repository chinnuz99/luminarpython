#class:design pattern
#object:real word entity
#references:name that refers a memory location of a object
#class creating
#class name start with cap letter
#class; in class function>method
#in class many methods are possible
#object creating in reference

class Person:                        #here person is class
    def walk(self):
        print("person is walking")
    def jumb(self):
        print("person is jumbing")
obj=Person()                         #here obj is reference
obj.walk()
obj.jumb()
obj2=Person()
obj2.walk()
obj2.jumb()



