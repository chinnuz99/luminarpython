dict={'name':'zara','age':7,'class':'first'}
print(dict)
print(type(dict))
print("dict['name']:",dict['name'])
print("dict['age']:",dict['age'])
print("dict['class']:",dict['class'])
#in dictionary keys is not repeted.
#in dictionary order satisfied.
#dictionary mutable.

#empty dictionary
dic={}
print(dic)
print(type(dic))

#elements change
dict={'name':'zara','age':7,'class':'first'}
dict['age']=8 #update existing entry
dict['school']="DPS school" #add new entry
dict.update({'loaction':'kochi'})
print(dict)

#remove entry
dict={'name':'zara','age':7,'class':'first'}
del dict['name'] #remove entry with keys "name
dict.clear() #remove all entries in dict
del dict #delete entire dictionary #dictionary is mutable
print(dict)