import re
x="[abc]"    #either a,b or c
matcher= re.finditer(x,"abt c74hbn")
for match in matcher:
    print(match.start())
    print(match.group())