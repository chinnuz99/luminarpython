#combination of lower case and upper case end with number
import re
n=input("enter")
x="([a-zA-Z]+\d$)"
match= re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")