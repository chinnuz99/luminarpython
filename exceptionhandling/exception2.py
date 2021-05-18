#using exception handling print index out of range
lst=[1,2,5,6]
n=int(input("enter index"))
try:
    print(lst[n])
except:
    print("exception occured")
finally:
    print("inside finally")


#at a time try or except is work
#finally work anytime in try and except

