import re
n="hello"
x='\w*'            #"\w" word including special character,  "a*" count including zero number of a
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
#
# import re
# n = "hello*-+"
# x = '\w*'  # "\w" word including special character,  "a*" count including zero number of a
# match = re.fullmatch(x, n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")