employees = [
          {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
          {"eid": 1001, "name": "vijay", "salary": 22000, "designation": "developer"},
          {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
          {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
          {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
     ]
#1)  print employeee names onlymap()
e_name=[emp['name'] for emp in employees]
print(e_name)

#2)  print all employee name into uppercase map()
upp_name=[emp["name"].upper() for emp in employees]
print(upp_name)

#3)  print employee details whose name starting with 'a'==a filter()
a_name=[emp["name"]for emp in employees if emp["name"][0]=='a']
print(a_name)

#4)  print employee details whose salary>23000 filter()
sal_emp=[emp["name"]for emp in employees if emp["salary"]>23000]
print(sal_emp)

#5)  in developers whose salary above 24000
developers=[emp["name"]for emp in employees if emp["designation"]=="developer" and emp ["salary"]>24000]
print(developers)