#binary search;split elements with midterm then check less or greater
a=[2,4,7,3,56,89,1,79,35,49,78]
print(a)
def bsearch():
    a.sort()
    print(a)
    ele=int(input("enter the element"))
    flag=0
    low=0
    upp=len(a)-1
    print(upp)
    while low<=upp:
        mid=(low+upp)//2
        if ele>a[mid]:
            low=mid+1
        elif ele<a[mid]:
            upp=mid-1
        elif ele==a[mid]:
            flag=1
            break
    if flag==1:
        print("found")
    else:
        print("not found")
bsearch()



