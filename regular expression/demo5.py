import re
x='[a-zA-Z]'            #both lower and upper case are checked
matcher= re.finditer(x,"abZt c74hzAbn")
for match in matcher:
    print(match.start())
    print(match.group())