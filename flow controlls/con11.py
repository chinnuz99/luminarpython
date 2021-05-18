age=int(input("enter ur age"))
sex=input("enter ur sex male(m),female(f):")
martialstatus=input("enter ur martial status single(n),married(y):")
if(sex=="f"):
    print("you can wrk at urban areas")
elif(sex=="m")&(age>=20 and age<=40):
    print("you can work anywhere")
elif(sex=="m")&(age>=40 and age<=60):
    print("you can work in urban areas")
else:
    print("error")
