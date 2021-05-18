#sorting the list in ascending order
# a=[2,8,9,56,7,6,86,5,12,90,46,35,100,63,11,4,1,52]
# print(a)
# a.sort()
# print("sorted in ascending order:",a)
#sorting in descending order
# a=[2,8,9,56,7,6,86,5,12,90,46,35,100,63,11,4,1,52]
# print(a)
# a.sort(reverse=True)
# print("sorted in descending order:",a)

#sorting the list in ascending number
my_list=[111,-15,-26,15,1,0,8,876,100,54,23,-64,23,76]
print(my_list)
new_list=[]
while my_list:
    min=my_list[0]  #0th num=111 ,111
    for i in my_list:
        if i<min: #111<(-15) ,111<876
            min=i #false ,true min=876
    new_list.append(min) #true,876add
    my_list.remove(min) #true,876remove
print(new_list)

