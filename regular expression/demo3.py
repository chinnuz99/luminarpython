import re
x="[a-z]"       #a to z
matcher=re.finditer(x,"a-z")
for match in matcher:
    print(match.start())
    print(match.group())