#pattern matching
# re(regular expression)__package for pattern matching
#finditer(method in regular expression)
#used for itrating
# import re
# count=0
# matcher=re.finditer('ab','abaaabbab')
# #print(matcher)
# for match in matcher:
#     count+=1
# print("count=",count)


import re
count=0
matcher=re.finditer('ab','abaabab')
for match in matcher:
    print("match available at",match.start())      #return positions
    print("group",match.group())                   #which object find match
    count+=1
print("count=",count)






