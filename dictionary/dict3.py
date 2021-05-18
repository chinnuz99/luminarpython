#key present or not
dict={'name':'parvathy','age':22,'place':'kottayam'}
# a=input("enter the key")
# for i in dict:
#     if i==a:
#         print("present")
#         break
# else:
#     print("not present")

#using function
def is_key_present(x):
    if x in dict:
        print(x,'is present in the dictionary')
    else:
        print(x,'is not present in the dictionary')
is_key_present('parvathy')
is_key_present('name')

