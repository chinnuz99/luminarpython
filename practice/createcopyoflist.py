a=[17,24,15,30,34,27]
b=a.copy()
print("original list:",a)
print("crated list:",b)
a[0]+=10
b[-1]+=10
print("original list:",a)
print("created list after change:",b)