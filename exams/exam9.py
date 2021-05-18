#Write a Python program to find the sequences of one upper case letter followed by lower case letters?
import re
n=input("enter")
x="[A-Z][a-z]*"    #x='[A-Z][a-z]+$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
