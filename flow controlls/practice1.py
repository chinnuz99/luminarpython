sal=int(input("enter ur salary"))
initial=int(input("enter ur joining year"))
final=int(input("enter ur current year"))
bonus=(5/100)*sal
year=final-initial
if(year>=5):
    newsal=bonus+sal
    print(newsal)
else:
    print("experience less than 5")