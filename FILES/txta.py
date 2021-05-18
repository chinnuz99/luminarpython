f1=open("txt1.txt", "r")
f2=open("txt2.txt",'w')
for i in f1:
    f2.write(i)