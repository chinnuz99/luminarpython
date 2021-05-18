# arr=[2,3,4,5,6]
# def square(num):
#     return num**2
# #map(function,iterable)
# squarelist=list(map(square,arr))
# print(squarelist)

arr=[2,3,4,5,6]
squarelist=list(map(lambda num:num**2,arr))
print(squarelist)

# lst=["ajay","arun","nikil","nivin"]
# def to_upper(name):
#print names in uppercase letters
lst=["ajay","arun","nikil","nivin"]
uppername=list(map(lambda name:name.upper(),lst))
print(uppername)
