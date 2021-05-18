import re
x='[A-Z]'   #A to Z
matcher= re.finditer(x,"Abt c74hbZn")
for match in matcher:
    print(match.start())
    print(match.group())