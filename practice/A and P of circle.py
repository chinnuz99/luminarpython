#program to display a menu for calculating area of a circle or perimeter of a circle
radius=float(input("enter the radius:"))
print("1.calclate area")
print("2.calculate perimeter")
choice=int(input("enter ur choice:"))
if choice==1:
    area=3.14*radius*radius
    print("area of circle with radius",radius,'is',area)
else:
    perimeter=2*3.14*radius
    print("perimeter of circle with radius",radius,'is',perimeter)