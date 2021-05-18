import re
x='\s'                #check space
matcher= re.finditer(x,"ab11Zt ch49zAbn")
for match in matcher:
    print(match.start())
    print(match.group())