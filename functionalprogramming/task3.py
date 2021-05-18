
employees = [
          {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
          {"eid": 1001, "name": "vijay", "salary": 22000, "designation": "developer"},
          {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
          {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
          {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
     ]
#1)  print employeee names onlymap()
e_names=list(map(lambda emp:emp["name"],employees))
print(e_names)


#2)  print all employee name into uppercase map()
up_names=list(map(lambda name:name.upper(),e_names))
print(up_names)

#3)  print employee details whose name starting with 'a'==a filter()
a_names=list(filter(lambda emp:emp["name"][0]=='a',employees))
print(a_names)

#4)  print employee details whose salary>23000 filter()
sal_emp=list(filter(lambda emp:emp["salary"]>23000,employees))
print(sal_emp)

#5)  print employee details whose designation==developer
developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
print(developers)

#6)  in developers whose salary above 24000
developers=list(filter(lambda emp:emp["designation"]=="developer"and emp["salary"]>24000,employees))
print(developers)

#6)  print highest salary
from functools import *
high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                   list(map(lambda emp:emp["salary"],employees)))
print("highest salary:",high_sal)

# # mysql community dowload ,
# # password:Password@123


