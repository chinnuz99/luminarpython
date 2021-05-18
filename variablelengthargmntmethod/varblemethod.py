# #add
# def add(num1,num2):  #para1 ,para2
#      return num1+num2
#  res=add(10,20)       #arg1,arg2
#  print(res)
#
# def add_three(num1,num2,num3):
#     return num1+num2+num3
# def add_four(num1,num2,num3,num4):
#
#
# #add three
# #addThree() first -camalin notation
# #add_three() second
# #python
# #Person   first snake notation
# #person
#
#
#
# def add(*args):       #(*args)it will accept any number of arguments(including zero number of argumnts) in the form of tuple.
#     print(type(args))
# add(10)
# add(10,20)
# add(10,20,30)

# def add(*args):      #args=(10,20)
#     res=0
#     for num in args:  #10
#         res+=num      #res=0+10=10+20=30
#     return res        #30
# print(add(10,20,30,40))



# def print_employee(**kwarges):
#     print(kwarges)
#     for k,v kwarges.items():
#         print(k"=>",v)
#
# print_employee(id=100,nat_place="thrissur",job="kakkanad")

# def print_employee(**kwargs):
#     print(kwargs)
# print_employee(id=1000,name="ajay",salary=5000)

#


# arr=[10,8,11,9,12]
# #arr.sort(reverse=true)       #method
# srt=sorted(arr,reverse=True)   #function()
# print(srt)
#
#
# def mysort():
#     print("inside sort function")
# class Mylist:
#     def mysortmeth(self):
#         print("inside sort method")
# mysort()
# obj=Mylist()
# obj.mysortmeth()
#

#difeerence b/w
# *args >tuple
# **kwargs>dictionary

#create a function print_employee(id=1000)=>name of that employee

employees={
     1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001:{"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
    1002:{"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
    1003:{"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
    1004:{"eid":1004,"name":"ram","salary":20000,"designation":"mrkt"},
}
# def print_employee(**kwargs):      #kwargs={id:10000}
#      employees = {
#          1000: {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
#          1001: {"eid": 1001, "name": "vijay", "salary": 22000, "designation": "developer"},
#          1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#          1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#          1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#      }
#      for k,v in kwargs.items():
#          for i in employees:
#              if v==i:
#                  print(employees[i]["name"])
# print_employee(id=1000)

def print_employees(**kwargs):      #kwargs={id:1000}
    id=kwargs["id"]                 #1000
    if id in employees:             #1000 in employees
        print(employees[id]["name"])  #employeees[1000]
    else:
        print("invalid id")
print_employees(id=1003)



#print_employee(id=1000)=>ajay
#print_employee(id=1000,prop="salary")ajay,25000
#print_employee(id=1001,prop="sdesignation")vijay,developer

