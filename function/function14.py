#to remove symbols from string
#enter a string: hello:"""fhbjn$%^&
#helloofhbjn
str=input("enter the string")
b="!@#$%^&*}*(&)][{<>?:{}:"
c=" "
for i in str:
    if i not in b:
        c+=i #moving the string without symbols to new string
print(c)

