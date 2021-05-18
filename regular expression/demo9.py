import re
x='\d'            #check the digits
matcher= re.finditer(x,"ab11Zt ch49zAbn")
for match in matcher:
    print(match.start())
    print(match.group())