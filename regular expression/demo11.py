import re
x='\w'                #all words except special characters
matcher= re.finditer(x,"ab11Zt ch4#$9zAbn")
for match in matcher:
    print(match.start())
    print(match.group())